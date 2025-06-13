def faixa_etaria(idade):
    if 0 <= idade < 17:
        return 'Menor idade'
    elif idade in range(18, 64):
        return 'Maior idade'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'Idade inválida'
    
    
if __name__ == '__main__':
    for idade in (15, 0, 22, 67, 111, -10):
        print(f'{idade}: {faixa_etaria(idade)}')