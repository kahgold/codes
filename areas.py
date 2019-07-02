#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 16:53:25 2019

@author: katia
"""
pi = 3.14159
_input = input()
_input = _input.split()
A, B, C = [float(el) for el in _input]

area_tri = (A * C) / 2
area_circ = pi * (C**2)
area_trap = ((A + B) * C) / 2
area_quad = B * B
area_ret = A * B

print('TRIANGULO: %.3f' %area_tri)
print('CIRCULO: %.3f' %area_circ)
print('TRAPEZIO: %.3f' %area_trap)
print('QUADRADO: %.3f' %area_quad)
print('RETANGULO: %.3f' %area_ret)