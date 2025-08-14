#!/usr/local/bin/python3


lista_1 = [1,2,3]

dobro = map(lambda x: x * 2, lista_1)
#print(list(dobro))

lista_2 = [
    {'nome': 'Luan', 'idade': 20},
    {'nome': 'Lavinia', 'idade': 19},
    {'nome': 'Gabriel', 'idade': 18},
]

so_nomes = map(lambda p: p['nome'],lista_2)
#print(list(so_nomes))

so_idade = map(lambda p: p['idade'], lista_2)
#print(list(so_idade))

frases = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos.', lista_2)
print(list(frases))