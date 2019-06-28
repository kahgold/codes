#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 16:34:05 2019

@author: katia
"""

item1 = input().split()[1:]
item2 = input().split()[1:]
item1 = [float(it) for it in item1]
item2 = [float(it) for it in item2]

qty1, price1 = item1
qty2, price2 = item2
res = (qty1*price1) + (qty2*price2)

print('VALOR A PAGAR: R$ %.2f' %res)