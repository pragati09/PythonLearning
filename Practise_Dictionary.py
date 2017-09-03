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

print(list(tel.keys()))

print(sorted(tel.keys()))

print('guido' in tel)

print('jack' not in tel)

u=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(u)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

X=['tic', 'tac', 'toe']    
for i, v in enumerate(X):
    print(i, v)
    
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    
for i in reversed(range(1, 10, 2)):
    print(i)
    
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)