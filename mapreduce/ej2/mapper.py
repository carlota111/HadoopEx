#!/usr/bin/python
# -*- coding: utf-8 -*-

# O formato de cada liña é:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# Queremos os elementos 3 (categoría/item description) e 4 (cost)
# Imos escribir a saída no formato separado por tabuladores: categoría\tcusto

import sys

for line in sys.stdin:
    # Elimina espazos en branco e separa a liña por tabuladores
    data = line.strip().split("\t")

    # Comproba que a liña teña exactamente 6 elementos
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print(item + "\t" + cost)
    else:
        # Ignorar liñas mal formadas
        continue

