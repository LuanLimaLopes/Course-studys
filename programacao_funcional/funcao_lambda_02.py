#!/usr/local/bin/python3

buy = (
    {'quantity': 2, 'price':10},
    {'quantity': 3, 'price':20},
    {'quantity': 5, 'price':14},
)

def calc_preco_total(buying):
    return buying['quantity'] * buying['price']

totals = tuple(map(calc_preco_total, buy))


print('total prices: ', totals)
print('Grand total:', sum(totals))