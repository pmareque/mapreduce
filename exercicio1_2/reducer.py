#!/usr/bin/python

import sys

itemsTotal = 0
oldItem = None

for line in sys.stdin:

    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if oldItem and oldItem != line.strip():
       print(oldItem+"\t"+str(itemsTotal))
       oldItem = line.strip()
       itemsTotal = 0

    oldItem = line.strip()
    itemsTotal += 1

# Escribe o ultimo, unha vez rematado o bucle
if oldItem != None:
   print(oldItem+"\t"+str(itemsTotal))
