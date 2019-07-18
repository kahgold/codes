#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:13:56 2019

@author: katia
"""
X = float(input())  # valor com 4 casas decimais
N = [X]
for i in range(1, 99):
    Y = X / 2
    N.append(Y)
    print("N[{}] = {:.4f}". format(i, N[Y]))
