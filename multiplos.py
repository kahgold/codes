#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:21:29 2019

@author: katia
"""
N = input()
N = map(int, N.split())
A, B = N


if B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
