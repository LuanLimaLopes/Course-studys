#!/usr/local/bin/python3
# Usando append para retirar varieveis de penultimo e ultimo
def fibonnaci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == '__main__':
    for fib in fibonnaci(200):
        print(fib)