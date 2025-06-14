#!/usr/local/bin/python3

with open('pessoas.csv') as arquivo:
    # w para escrita
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            #file = saida, para direcionar na onde ele iria escrever
            print("Nome: {}, Idade: {}".format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo fechado')
#verificação se foi escrito corretamente
if saida.closed:
    print('Arquivo de escrita, foi fechado!')
    