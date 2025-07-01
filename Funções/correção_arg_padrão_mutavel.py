#!/usr/local/bin/python3 

def fibonacci(sequencia=None):
    #usando or para gerar valor default
    #não usar valor mutavel para metodos
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

if __name__ == '__main__':
    inicio = fibonacci()

    print(inicio, id(inicio))
    print(fibonacci(inicio))

    restart = fibonacci()
    print(restart, id(restart))
    