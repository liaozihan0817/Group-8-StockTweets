import json
inputFile = 'EndOf2015_8k.json'
fin = open(inputFile,'r')
lines = fin.readlines()
symbolDict = {}     # creat a new dict, symbolDict = dict()
sectorDict = {}    # This dict store the top ten symbols in different sectors
treeDict = {'name': "treemap", 'children': []}

#print ("Display created empty symbolDict:", symbolDict)

for i in range(0, 7999):
    data = json.loads(lines[i])
#    print("\nmessage_id:", data['id'])
#    print (data.keys())  # print the keys of a message
    if "symbols" in data:  # check if key "symbols" is in the entry(dict object)
        for SYMBOL in data['symbols']:
#            print (SYMBOL.keys())  # print the keys of a symbol
#            print (SYMBOL)  # print the entry for a symbol
#            print("    ", "symbol_id:", SYMBOL['id'],"    ", "symbol:", SYMBOL['symbol'])
            
            # calculating message volume of a symbol
            if SYMBOL['symbol'] in symbolDict:
                symbolDict[SYMBOL['symbol']]['count'] += 1
            else:
                symbolDict[SYMBOL['symbol']] = SYMBOL;
                symbolDict[SYMBOL['symbol']]['count'] = 1
                symbolDict[SYMBOL['symbol']]['relatedSymbol'] = {}
            
            # calculating the other symbols mention together
            for RELATEDSYMBOLS in data['symbols']:
                if RELATEDSYMBOLS['symbol'] != SYMBOL['symbol'] and RELATEDSYMBOLS['symbol'] in symbolDict[SYMBOL['symbol']]['relatedSymbol']:
                    symbolDict[SYMBOL['symbol']]['relatedSymbol'][RELATEDSYMBOLS['symbol']] += 1
                elif RELATEDSYMBOLS['symbol'] != SYMBOL['symbol']:
                    symbolDict[SYMBOL['symbol']]['relatedSymbol'][RELATEDSYMBOLS['symbol']] =1

# convert relatedSymbol subDict to a sorted list relatedSymbolList
for STOCK in symbolDict:
    symbolDict[STOCK]['relatedSymbolList'] = []
    for relatedSymbols in symbolDict[STOCK]['relatedSymbol']:
        symbolDict[STOCK]['relatedSymbolList'].append({'name': relatedSymbols,
                                                       'relate_count': symbolDict[STOCK]['relatedSymbol'][relatedSymbols]})
    symbolDict[STOCK]['relatedSymbolList'].sort(key = lambda x: x['relate_count'], reverse = True)
    del symbolDict[STOCK]['relatedSymbolList'][5:]    # truncate relatedSymbolList, leave at most 5 related symbols.
    del symbolDict[STOCK]['relatedSymbol']    # delete a key value pair in dictionary

#convert dict to object and store objects into a list
symbolList = []    #This is a list of objects

class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)

for TICKER in symbolDict:
    tempSymbol = symbolDict[TICKER]
    temp = Struct(**tempSymbol)    # Don't know why it works
    symbolList.append(temp)

#            print ("    ", "sector:", symbolDict[SYMBOL['symbol']]['sector'])

#print (symbolDict.keys())
#print (symbolDict)

#for ticker in symbolDict:
#    print (symbolDict[ticker]["symbol"], symbolDict[ticker]["count"])    #print generated symbolDict

with open('symbolDict.json', 'w') as f:
    json.dump(symbolDict, f, sort_keys=True, indent=4)
    for item in symbolDict.items():
        json.dump(item, f)
        f.write('\n')

symbolList.sort(key = lambda x: x.count, reverse = True)
#try not convert to object, just use x['count'] to sort next time.
#print (symbolList)

#for ITEM in symbolList:
#    print (ITEM.count)

# store symbols with top ten largest volume
symbolSorted = []    # a list used to store sorted symbols. This is a list of dict
for i in range(0,10):
#    print (symbolList[i].symbol)
    symbolSorted.append(symbolDict[symbolList[i].symbol])
    if symbolList[i].sector in sectorDict:
        sectorDict[symbolList[i].sector].append({'name': symbolDict[symbolList[i].symbol]['symbol'],
                                                 'value': symbolDict[symbolList[i].symbol]['count'],
                                                 'title': symbolDict[symbolList[i].symbol]['title'],
                                                 'exchange': symbolDict[symbolList[i].symbol]['exchange'],
                                                 'relatedSymbols': symbolDict[symbolList[i].symbol]['relatedSymbolList']})
#        sectorDict[symbolList[i].sector].append(symbolDict[symbolList[i].symbol])
    else:
        sectorDict[symbolList[i].sector] = []
        sectorDict[symbolList[i].sector].append({'name': symbolDict[symbolList[i].symbol]['symbol'],
                                                 'value': symbolDict[symbolList[i].symbol]['count'],
                                                 'title': symbolDict[symbolList[i].symbol]['title'],
                                                 'exchange': symbolDict[symbolList[i].symbol]['exchange'],
                                                 'relatedSymbols': symbolDict[symbolList[i].symbol]['relatedSymbolList']})

#print ("sectorDict length:", len(sectorDict))

#with open('sectorDict.json', 'w') as f:
#    json.dump(sectorDict, f)

#symbolTen = dict(symbolSorted)

#print (sectorDict)

#try to build a children list
sectorList = []

for SECTOR in sectorDict:
    sectorList.append({'name': SECTOR, 'children': sectorDict[SECTOR]})

#print (sectorList)

#Set the value of first level 'children' to be sectorList
treeDict['children'] = sectorList

with open('TreemapDict.json', 'w') as f:
#    for item in treeDict.items():
        json.dump(treeDict, f)
#        f.write('\n')
