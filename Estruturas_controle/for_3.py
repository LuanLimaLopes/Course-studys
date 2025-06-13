mercado = {'Produto': 'Garrafa', 'Preco': 10, 'Embalagem': 'Plastico', 'Importada': True, 'Estoque': 798}

for chaves in mercado:
    print(chaves)

for valor in mercado.values():
    print(valor)

for chave, valor in mercado.items():
    print(chave, ' == ', valor)