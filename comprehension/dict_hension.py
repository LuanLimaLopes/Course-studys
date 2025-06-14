# generator ()
# Dict {}
# list comprehension []
dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)

for numeros, dobro in dicionario.items():
    print(f'{numeros} x 2 = {dobro}')