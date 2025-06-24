def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma

if __name__ == '__main__':
    #Unpacking
    nums = (2, 2, 2)
    print(soma_n(*nums))

    #Packing
    print(soma_n(2, 5))