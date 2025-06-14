#!/usr/local/bin/python3

import csv
#csv.reader faz o split/strip de forma automática
with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print("Nome:{}, Idade:{}".format(*pessoa))