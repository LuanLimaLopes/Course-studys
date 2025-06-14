#!/usr/local/bin/python3
# Usando for no lugar do while true e retirando o uso do len
def fibonacci(quant, sequencia=(0, 1)):
    #Condição de parada
    if len(sequencia) == quant:
        return sequencia
    return fibonacci(quant, sequencia + (sum(sequencia[-2:]), ))

if __name__ == '__main__':
    #Listar a quantidade de vezes que vai funcionar(fibonacci(quantidade))
    for fib in fibonacci(20):
        print(fib)

