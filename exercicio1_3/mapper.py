#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab
#
# obter a venda máis alta para cada tipo de pago 
# das rexistradas en todo o ficheiro

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
       date, time, store, item, cost, payment = data
       print(str(payment)+"\t"+str(cost))

