#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 12:18:21 2019

@author: katia
"""

idade = int(input()) 

anos = idade // 365
meses = (idade - anos *  365) // 30
dias = (idade - anos * 365 - meses * 30) 



print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(anos, meses, dias))