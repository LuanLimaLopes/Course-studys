# [ expressão, for item in list if condicional ]
#list comprehension
dobros = [x * 2 for x in range(1, 11)]
print(dobros)

#Versão normal
dobro = []
for x in range(10):
    dobro.append(x * 2)
print(dobro)
