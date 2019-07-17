#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:51:52 2019

@author: katia
1173
"""
V = int(input())
X = [V]

for i in range(10):
    X.append(V * 2 ** i)
    print("N[{}] = {}". format(i, X[i]))
