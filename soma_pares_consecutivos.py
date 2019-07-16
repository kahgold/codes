#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:52:41 2019

@author: katia
1159
"""

while 1:
    _input = int(input())
    if _input == 0:
        break
    _input = _input if _input % 2 == 0 else _input + 1
    soma = _input
    for i in range(4):
        _input += 2
        soma += _input
    print(soma)
