#!/usr/local/bin/python3

def mapear(fuction, list):
    for element in list:
        yield fuction(element)


if __name__ == '__main__':
    resultado = mapear(lambda x: x ** 2, [2,3,4])
    print(list(resultado))
    #print(list(mapear(lambda x: x ** 2, [2, 3, 4])))