# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 11:23:26 2017

@author: pragagupta
"""

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

list(tel.keys())

sorted(tel.keys())

print('guido' in tel)

print('jack' not in tel)
