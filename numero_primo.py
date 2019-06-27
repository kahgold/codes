#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:56:26 2019

@author: katia
"""
N = int(input())


for i in range(1, N):
    _input = input()
    _input = int, _input.split()


def ehPrimo(_input):
    divisores = 0
    i = 1
    while i <= _input:
        if _input % i == 0:
            divisores += 1
        i += 1
    if divisores == 2:
        print("X eh primo")
        return True
    else:
        print("X nao eh primo")
        return False


ehPrimo(_input)
