#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:03:51 2019

@author: katia
"""
N = int(input())

for i in range(1, N + 1):
    i2 = i ** 2
    i3 = i ** 3
    print(i, i2, i3)
    print(i, i2 + 1, i3 + 1)
