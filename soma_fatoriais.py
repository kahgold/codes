#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:51:56 2019

@author: katia
"""
M = 0
N = 0

while M <= 20 and N <= 20:
    _input = input()
    _input = map(float, _input.split())
    M, N = _input


fat = 1
_fat = 1
for i in range(1, N + 1):
    fat = fat * i
for j in range(1, M + 1):
    _fat = _fat * j

soma = fat + _fat

print(soma)
