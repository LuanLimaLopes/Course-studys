#!/usr/local/bin/python3

def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular

if __name__ == "__main__":
    dobro = multiplicar(2)
    triplo = multiplicar(3)

    print(f'O dobro de 5 é {dobro(5)}')
    print(f'O triplo de 5 é {triplo(5)}')