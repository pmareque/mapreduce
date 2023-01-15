#!/usr/bin/python

# obter a venda máis alta para cada tipo de pago

import sys

highPrice = 0
oldPayment = None

for line in sys.stdin:

    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
       continue

    payment, sale = data_mapped

    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if oldPayment and oldPayment != payment:
       print(oldPayment+"\t"+str(highPrice))
       oldPayment = payment
       highPrice = 0

    oldPayment = payment
    if float(sale) > float(highPrice):
       highPrice = sale

# Escribe o ultimo, unha vez rematado o bucle
if oldPayment != None:
   print(oldPayment+"\t"+str(highPrice))
