#Generator é muito mais leve do que o list comprehension mas gera sob demanda.
#Comprehesion ocupa os espaço em memória

generator = (i ** 2 for i in range(10) if i % 2 == 0)
# print(next(generator))

for numero in generator:
    print(numero)