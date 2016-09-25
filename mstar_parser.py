'''
Created on Aug 28, 2016

@author: Prasad
'''
outformat = "{0},{1},{2}"
with open("mstar.txt", "r") as f:
    for line in f:
        splits = line.split("#")
        
        if len(splits) != 3:
            continue
        
        category = splits[0].split("|")[0]
        dates = splits[1].split("|")
        indices = splits[2].split("|")
        last = len(dates) - 1
        print outformat.format(category, dates[last], indices[last])