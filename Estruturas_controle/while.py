from random import randint

num_inform = -1
num_sec = randint(0,9)

while num_inform != num_sec:
    num_inform = int(input('Informe o número secreto: '))

print("O número secreto {} Foi encontrado!!".format(num_sec))