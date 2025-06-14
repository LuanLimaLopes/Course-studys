# [ expressão, for item in list if condicional ]
# list comprehension

triplo = [i * 3 for i in range(1, 11) if i % 2 == 1]
print(f"List comprehesion: {triplo}")

# versão normal
triplos = []
for i in range(1, 11):
    if i % 2 == 1:
        triplos.append(i * 3)
print(f"Lista normal: {triplos}")