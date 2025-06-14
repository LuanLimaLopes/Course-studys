#!/usr/local/bin/python3
#Try finally, o finally é executado independente se houve erros no try
try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print("Nome: {}, Idade: {}".format(*registro.strip().split(',')))
   #except IndexError:
    #pass 
finally:
    arquivo.close()
#Verifica se o arquivo foi fechado corretamente e printa uma mensagem
if arquivo.closed:
    print('Arquivo foi fechado!')