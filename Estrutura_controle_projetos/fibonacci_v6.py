#!/usr/local/bin/python3
# Usando len para limitar a quantidade de numeros que eu quero
def fibonnaci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    for fib in fibonnaci(10):
        print(fib)