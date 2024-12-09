#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

maxSale = 0
oldPaymentType = None

# Loop para procesar os datos
# O formato será key\tval, onde key é o método de pago e val é o custo

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Algo saíu mal, ignorar esta liña
        continue

    thisPaymentType, thisSale = data_mapped

    try:
        thisSale = float(thisSale)
    except ValueError:
        # Ignorar valores de venda non numéricos
        continue

    # Se hai un cambio na clave (método de pago), escribimos o valor máximo
    if oldPaymentType and oldPaymentType != thisPaymentType:
        print(oldPaymentType + "\t" + str(maxSale))
        oldPaymentType = thisPaymentType
        maxSale = 0

    oldPaymentType = thisPaymentType
    maxSale = max(maxSale, thisSale)

# Escribe o último par clave:valor
if oldPaymentType is not None:
    print(oldPaymentType + "\t" + str(maxSale))

