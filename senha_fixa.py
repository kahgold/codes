#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:43:41 2019

@author: katia
1114
"""
N = int(input())

while N != 2002:
    print("Senha Invalida")
    N = int(input())
    if N == 2002:
        print("Acesso Permitido")
