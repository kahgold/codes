#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:50:06 2019

@author: katia
2234
"""
_input = input()
_input = map(float, _input.split())
H, P = _input

media = H / P
print("{:.2f}".format(media))
