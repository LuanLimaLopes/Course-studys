#!/usr/local/bin/python3
# Usando for no lugar do while true e retirando o uso do len
def fibonnaci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonnaci(10):
        print(fib)