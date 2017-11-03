# -*- coding: utf-8 -*-
from function import my_abs

d = {'Peter':95,'Bob':78,'Jack':88}
print(d['Peter'])

d['Adam'] = 99
print(d['Adam'])

b = 'Black' in d
print(b)

c = d.get('Black')
print(c)

e = d.get('Black',-2)
print(e)

f = d.get('Bob')
print(f)

print(set([1,2,3]))

print(my_abs(-6))
