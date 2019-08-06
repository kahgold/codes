#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:11:21 2019

@author: katia
"""
def validate_pass(passwd):
    punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~´`" "'''
    if len(passwd) < 6 or len(passwd) > 32:
        return False
    no_punct = [let in punctuation for let in passwd]
    if any(no_punct):
        return False
    _upper = [let == let.upper() and not let.isdigit() for let in passwd]
    _lower = [let == let.lower() and not let.isdigit() for let in passwd]
    if len(_upper) == 0 or len(_lower) == 0:
        return False
    number = [let.isdigit() for let in passwd]
    if not any(number):
        return False
    return True

# S = 0

# for i in range(S + 1):
S = input()
S = S.split('\n')
res_str = []
for ss in S:
    res = validate_pass(ss)
    if res:
        res_str.append("Senha valida.")
    else:
        res_str.append("Senha invalida.")
res_str = '\n'.join(res_str)
print(res_str)