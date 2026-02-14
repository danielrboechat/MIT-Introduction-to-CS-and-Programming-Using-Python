# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 19:35:31 2026

@author: Boechat
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    charNumber = len(aStr)
    if aStr == '':
        return False
    if char == aStr[charNumber//2]:
        return True
    elif char < aStr[charNumber//2]:
        return isIn(char,aStr[:charNumber//2])
    elif char > aStr[charNumber//2]:
        return isIn(char,aStr[(charNumber//2)+1:])
print(isIn('e','abcd'))