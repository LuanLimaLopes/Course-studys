#!/usr/local/bin/python3
from funcao_primeira_classe import dobro,quadrado


def processar(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(i, "=>", funcao(i))

if __name__ == "__main__":
    processar('Quero o Dobro de 2', range(1, 11), dobro)
    processar('Quero o Quadrado do 2', range(1, 11), quadrado)