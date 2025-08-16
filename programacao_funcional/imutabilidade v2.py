from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

setlocale(LC_ALL, 'pt_BR')


def month_31(month): 
    return mdays[month] == 31
def get_name_month(month):
    return month_name[month]
def all_month(all, name_month):
    return f'{all} \n- {name_month}'

print(reduce(all_month,
             map(get_name_month,
                  filter(month_31, range(1, 13))),
                'Meses com 31 dias:'
             ))