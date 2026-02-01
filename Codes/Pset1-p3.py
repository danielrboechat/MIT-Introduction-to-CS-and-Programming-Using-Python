# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 07:00:29 2026

@author: Boechat
"""

s='abckcde'
atual = s[0]
maior = s[0]
for i in range(1,len(s)):
    if s[i] >= s[i-1]:
        atual += s[i]
    else:
        atual = s[i]
    if len(atual) > len(maior):
        maior = atual
print('Longest substring in alphabetical order is:',maior)