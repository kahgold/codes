#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:49:07 2019

@author: katia
"""
tabela = {1: {'item': 'cach. q', 'price': 4.00}, 
          2: {'item': 'x-salada', 'price': 4.50}, 
          3: {'item': 'x-bacon', 'price': 5.00}, 
          4: {'item': 'torrada simples', 'price': 2.00},
          5: {'item': 'refri', 'price': 1.50}}

_input = input()
_input = _input.split()
code, qty = [float(el) for el in _input]

item = tabela.get(code)
price = item.get('price')
value = price * qty
print('Total: R$ %.2f' %value)
