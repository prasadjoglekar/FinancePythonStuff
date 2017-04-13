from ofxclient import Institution
from ofxparse import OfxParser
import ConfigParser

insts = None

def getInsts():
        
    config = ConfigParser.RawConfigParser()
    config.read('insts.properties')
    
    global insts
    if not insts:
        
        insts = {}
        for section in config.sections():
            inst = Institution(
                      id = config.get(section, "id"),
                      org = config.get(section, "org"),
                      url = config.get(section, 'url'),
                      username = '',
                      password = ''
            )
            
            insts[section] = inst
    


def pullForInst(inst, accountDict):
    
    for a in inst.accounts():
        if a.number == "20187":
            continue
        else:
            accountName = accountDict.get(a.number.upper())
            #internalsymbol    ext_symbol     quantity     date    action     price     commission    total_investment    broker    memo
            outputFormat = '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s'
            resp = a.download(10)
            ofx = OfxParser.parse(resp)
            transactions = ofx.account.statement.transactions
            for t in transactions:
                if t.type not in ['buydebt', 'buymf', 'buyopt', 'buyother', 'buystock', 'closureopt', 'income', 'invexpense', 'jrnlfund', 'jrnlsec', 'margininterest', 'reinvest', 'retofcap', 'selldebt', 'sellmf', 'sellopt', 'sellother', 'sellstock', 'split', 'transfer']:
                    continue
                print outputFormat % (t.security, '', str(t.units), str(t.tradeDate), '', str(t.unit_price), '', '',accountName, t.memo) 



if __name__ == "__main__":
            
    getInsts()
    #print insts
    
    config = ConfigParser.RawConfigParser()
    config.read('../pwds.properties')
      
    accountDict = {}
     
    for section in config.sections():
        accountProps = {}
        for k, v in config.items(section):
            if k.startswith("a"):
                accountProps[k[1:].upper()] = v
            else:
                accountProps[k] = v
        accountDict[section] = accountProps
    #print accountDict
      
    for k,v in insts.iteritems():
        if k == "Fidelity": 
            continue
        accountProps = accountDict[k]
        v.username = accountProps["username"]
        v.password = accountProps["password"]
        pullForInst(v, accountProps)