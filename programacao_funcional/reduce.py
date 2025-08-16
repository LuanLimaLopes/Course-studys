#!/usr/local/bin/python3
from functools import reduce

people = [
    {'name': 'Pedro', 'age': 20},
    {'name': 'Lavinia', 'age': 19},
    {'name': 'Luan', 'age': 20},
    {'name': 'Arthur', 'age': 26},
    {'name': 'Rebeca', 'age': 17},
    {'name': 'Aline', 'age': 17},
]

ages = map(lambda p: p['age'], people)
youghers = filter(lambda i: i < 18, ages)
sum_ages = reduce(lambda age, i: age + i, youghers, 0)

print(sum_ages)