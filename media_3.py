#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:10:12 2019

@author: katia
"""

nota = input()
nota = map(float, nota.split())
A, B, C, D = nota


media = (A * 2 + B * 3 + C * 4 + D * 1) / 10
print("Media: %.1f" % media)

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")

if media > 5 and media < 6.9:
    print("Aluno em exame.")

nota_exame = float(input())
print("Nota do exame: %.1f" % nota_exame)


nova_media = (nota_exame + media) / 2
if nova_media >= 5:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")
print("Media final: %.1f" % nova_media)
