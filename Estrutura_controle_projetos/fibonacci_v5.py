#!/usr/local/bin/python3
# Usando append + sum para ir do penultimo para o ultimo digito [-2:]
def fibonnaci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonnaci(200):
        print(fib)