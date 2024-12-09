#!/usr/bin/python
# -*- coding: utf-8 -*-

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    # Elimina espazos en branco e separa a liña por tabuladores
    data = line.strip().split("\t")
    
    # Comproba que a liña teña exactamente 6 elementos
    if len(data) == 6:
        date, time, store, item, cost, payment = data
	print(store+"\t"+cost)
    else:
        # Ignorar liñas mal formadas
        continue
