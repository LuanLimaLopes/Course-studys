#!/usr/local/bin/python3
#Bloco with, abre e fecha o arquivo automaticamente
#Mais seguro pq o proprio bloco fecha automaticamente o arquivo
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print("Nome: {}, Idade: {}".format(*registro.strip().split(',')))
#verificação se fechou
if arquivo.closed:
    print('Arquivo fechado')
    