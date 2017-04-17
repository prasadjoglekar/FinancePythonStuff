'''
Created on Aug 28, 2016

@author: Prasad
'''

industryFile = "mstar_industry.txt"
sectorFile = "mstar_sector.txt"

fileToUse = industryFile

outformat = "{0},{1},{2}"
with open(fileToUse, "r") as f:
    for line in f:
        splits = line.split("#")
        
        if len(splits) != 3:
            continue
        
        category = splits[0].split("|")[0]
        dates = splits[2].split("|")
        indices = splits[1].split("|")
        last = len(dates) - 3
        print outformat.format(category, dates[last], indices[last])