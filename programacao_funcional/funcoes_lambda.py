#!/usr/local/bin/python3

buy = (
    {'quantity': 2, 'price':10},
    {'quantity': 3, 'price':20},
    {'quantity': 5, 'price':14},
)

totals = tuple(
    map(
        lambda buying: buying['quantity'] * buying['price'],
        buy
    )
)

print('total prices: ', list(totals))
print('Grand total:', sum(totals))