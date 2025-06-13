def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda-feira',
        3: 'Terça-feira',
        4: 'Quarta-feira',
        5: 'Quinta-feira',
        6: 'Sexta-feira',
        7: 'Sábado'
    }
    return dias.get(dia, "** INVÁLIDO **")

if __name__ == '__main__':
    for dia in range(0, 9):
        if dia == 1 or dia == 7:
            print(f"{dia}: {get_dia_semana(dia)} Esse dia e final de semana!")
        else:
            print(f'{dia}: {get_dia_semana(dia)}')