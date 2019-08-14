#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:05:11 2019

@author: katia
"""
qntteste = int(input())
repetidor1 = 0
repetidor2 = 0
repetidor3 = 0
qntled = 0
listaleds = ["0"]*qntteste


while qntteste > repetidor1:
    repetidor2 = 0
    qntled = 0
    njoao = input()
    numeros = list(map(int, njoao.split()))
    lennum = len(njoao)
    while lennum > repetidor2:
        if njoao[repetidor2] == "0" or njoao[repetidor2] == "6" or njoao[repetidor2] == "9":
            qntled += 6
        elif njoao[repetidor2] == "1":
            qntled += 2
        elif njoao[repetidor2] == "2" or njoao[repetidor2] == "3" or njoao[repetidor2] == "5":
            qntled += 5
        elif njoao[repetidor2] == "4":
            qntled += 4
        elif njoao[repetidor2] == "7":
            qntled += 3
        elif njoao[repetidor2] == "8":
            qntled += 7
        listaleds[repetidor1] = qntled
        repetidor2 += 1
    repetidor1 += 1
while qntteste > repetidor3:
    print(listaleds[repetidor3], "leds")
    repetidor3 += 1
