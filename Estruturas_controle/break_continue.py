#Valida o resultado e continua
for x in range(1, 11):
    if x % 2 == 1:
        continue
    print(x)
#Valida o resultado e para se for True
for x in range(1, 11):
    if x == 7:
        break
    print(x)

print('fim!')