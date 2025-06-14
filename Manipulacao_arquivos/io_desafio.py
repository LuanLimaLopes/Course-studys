#!/usr/local/bin/python3

import csv
from urllib import request

def read(url):
    with request.urlopen(url) as entrada:
        print("Baixando CSV do IBGE...")
        dados = entrada.read().decode('latin1')
        print("Download do CSV completo!!")
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[3]}: {cidade[8]}')

if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
