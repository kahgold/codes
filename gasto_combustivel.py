#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:37:47 2019

@author: katia
"""
autom = 12 #12 km/L
h_gastas = int(input()) #tempo gasto na viagem (horas)
veloc = int(input()) #veloc média (km/h)
dist = h_gastas * veloc #distância percorrida (km)
litros = dist / autom #calcula a quantidade de litros gastos
print("%.3f" %litros)