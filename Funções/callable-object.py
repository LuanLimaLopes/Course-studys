#!/usr/local/bin/python3

#construtor em py __init__()
#self instância atual
#Exige um parâmetro obrigatório
#Função chamada para um objeto __call__


class calc:
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente
    
if __name__ == '__main__':
    quadrado = calc(2)
    cubo = calc(3)

    if callable(quadrado) and callable(cubo):
        print(f'3(2) => {quadrado(3)}')
        print(f'5(2) => {quadrado(5)}')

        print(f'2(3) => {cubo(2)}')
        print(f'4(3) => {cubo(4)}')