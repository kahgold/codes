#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:09:51 2019

@author: katia
1777
"""
T = int(input())
N = [T]

for i in range(0, T - 1):
    N.append(T * 2 ** i)
    print("N[{}] = {}". format(i, N[i]))
