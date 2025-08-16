#!/usr/local/bin/python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name

setlocale(LC_ALL, 'pt_BR')

print('Meses com 31 dias:')
for month in range(1,13):
    if mdays[month] == 31:
        print(f'- {month_name[month]}')