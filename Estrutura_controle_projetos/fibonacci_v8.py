#!/usr/local/bin/python3
# Usando for no lugar do while true e retirando o uso do len
def fibonnaci(maximo, atual):
    if maximo < atual:
        resultado = [0, 1]
        resultado.append(sum(resultado[-2:]))
        fibonnaci(maximo, atual)

