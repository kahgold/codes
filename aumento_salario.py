#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:19:48 2019

@author: katia
"""
tabela = {{'salario': '0 - 400.00', 'percentual': 15},
          {'salario1': '400.01 - 800.00', 'percentual1': 12},
          {'salario2': '800.01 - 1200.00', 'percentual2': 10},
          {'salario3': '1200.01 - 2000.00', 'percentual3': 7},
          {'salario4': 'Acima de 2000.00', 'percentual': 4}}

salary = float(input())
new_salary = salary * 