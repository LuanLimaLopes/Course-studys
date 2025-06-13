#Se I for true (7), ele para o código e não executa o restante (else)
#Se I for false (outro numero), ele avança no codigo e executa o (else)

#for i in range(1, 11):
#    if i == 7:
#        break
#    print(i)
#else:
#    print('fim!')
#

from random import randint

def sortear_dado():
    return randint(1,6)

for i in range(1,7):
    if i % 2 == 1:
        continue

    sorteio = sortear_dado()

    if i == sorteio:
        print(f"Você acertou!! numero sorteado foi: {sorteio} e seu número {i}")
        break

else:
    print(f"Você errou! numero sorteado foi: {sorteio} e seu número {i}")


