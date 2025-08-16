#!/usr/local/bin/python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses do ano com 31 dias

months_31 = filter(lambda month: mdays[month] == 31, range(1,13))
months_names = map(lambda month: month_name[month], months_31)
all_months = reduce(lambda all, name_month: f'{all}\n- {name_month}', months_names, 'Meses com 31 dias: ')

print(all_months)
