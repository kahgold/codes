#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:42:25 2019

@author: katia
"""

lados = input()
lados = map(float, lados.split())
A, B, C = lados

if ((A + B) > C) and ((A + C) > B) and ((B + C) > A):
    perimetro = A + B + C
    print("Perimetro = %.1f" % perimetro)
else:
    area = ((A + B) * C) / 2
    print("Area = %.1f" % area)
