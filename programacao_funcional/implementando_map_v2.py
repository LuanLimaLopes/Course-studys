#!/usr/local/bin/python3

def mapear(fuction, list):
    return (fuction(element) for element in list)


if __name__ == '__main__':
    resultado = mapear(lambda x: x ** 2, [2,3,4])
    #print(list(resultado))
    print(tuple(resultado))