# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 21:26:16 2026

@author: Boechat
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    res = b
    while a%res != 0 or b%res != 0:
           res -= 1
    return res
    
print(gcdIter(10, 10))

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    "a = q0xb+r0"
    quo = a//b
    res = a%b
    while res!=0:
        a=quo*b+res
        return gcdRecur(b,a%b)
    return b
print(gcdRecur(84,21))
"a vira b e b vira a%b"