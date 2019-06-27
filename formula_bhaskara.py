#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:27:32 2019

@author: katia
"""
import math


valor = input()
valor = map(float, valor.split())
A, B, C = valor

delta = B ** 2 - (4 * A * C)

raiz1 = (- B + math.sqrt(delta)) / (2 * A)
raiz2 = (- B - math.sqrt(delta)) / (2 * A)

print("R1 = {:.5f}".format(raiz1))
print("R2 = {:.5f}".format(raiz2))
if raiz1 < 0 and raiz2 < 0:
    print("Impossivel calcular")
if raiz1 / 0 and raiz2 / 0:
    print("Impossivel calcular")
