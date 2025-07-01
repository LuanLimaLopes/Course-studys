#!/usr/local/bin/python3

def log(function):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da função: {function.__name__}')
        print(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'resultado da chamada: {resultado}')
        return resultado
    return decorator

@log
def soma(x, y):
    return x + y
@log
def sub(x, y):
    return x - y

if __name__ == '__main__':
    valor = soma(5, 5)
    valor2 = sub(5, 2)
    print(valor)
    print(valor2)