#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:39:37 2019

@author: katia
"""
N = int(input())

for i in range(N):
    _input = input()
    _input = map(float, _input.split())
    A, B, C = _input
    media = ((A * 2) + (B * 3) + (C * 5)) / 10

print(media)
