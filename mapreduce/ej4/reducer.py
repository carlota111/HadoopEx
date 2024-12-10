#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

maxSale = 0  # Inicializamos a variable para o máximo absoluto

# Loop para procesar os datos
# O formato será key\tval, onde key é o método de pago e val é o custo

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Algo saíu mal, ignorar esta liña
        continue

    _, thisSale = data_mapped  # Non necesitamos a clave neste caso

    try:
        thisSale = float(thisSale)
    except ValueError:
        # Ignorar valores de venda non numéricos
        continue

    # Actualizamos o máximo absoluto
    maxSale = max(maxSale, thisSale)

# Escribe o máximo absoluto ao final
print("Máximo absoluto de vendas: " + str(maxSale))

