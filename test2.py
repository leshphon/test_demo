# coding=utf-8
from test1 import Cat
from functools import reduce

arr_list = [2] * 5
converEncodingStr = 'alter table table_name convert to character set utf8;'
my_cat = Cat('Deidei', 'white', 3)
my_cat.eat_rat(3)
new_str = converEncodingStr.replace('table_name', 'old_table', 1) # third argument mean times that replacement occurs
print(new_str)
print(arr_list)

def prod(x, y):
    return x * y
print(reduce(prod, [2, 4, 5, 7, 12], 2)) # reduce has three argements (iterated func, target arr, initial value)
print(reduce(lambda x, y: x * y, [2, 4, 5, 7, 12]))
