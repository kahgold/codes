#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:28:24 2019

@author: katia
"""
N = int(input())

# for i in range(N):
#     _input = input()
#    x = _input.split()

sum1 = 0
for i in range(1, N):
    if N % i == 0:
        sum1 += 1
    if sum1 == N:
        print("X eh perfeito")
    else:
        print("X nao eh perfeito")
