#!/usr/local/bin/python3 

def fibonacci(sequencia=[0,1]):
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

if __name__ == '__main__':
    inicio = fibonacci()

    print(inicio, id(inicio))
    print(fibonacci(inicio))

    #está sendo mutável, e está gerando erro.
    #Atributo mutável se comportando como default
    restart = fibonacci()
    print(restart, id(restart))
    