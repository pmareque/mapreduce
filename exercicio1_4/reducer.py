#!/usr/bin/python

import sys

highCost = {}

for line in sys.stdin:

    data = line.strip().split("\t")
    
    thisKey, thisSale = data
    if thisKey not in highCost.keys():
       highCost[thisKey] = float(thisSale)
    else:
       highCost[thisKey] += float(thisSale)

for key, cost in highCost.items():
    print(key + '\t' + str(cost))
