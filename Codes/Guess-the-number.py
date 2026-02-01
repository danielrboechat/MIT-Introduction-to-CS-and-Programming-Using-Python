# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 09:58:01 2026

@author: Boechat
"""
high = 100
low = 0
number = int((high+low)/2)
print('Please think of a number between 0 and 100!') 
print('Is your secret number', str(number) + '?')
ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while ans != 'c':
    if ans == 'h':
        high = number
        number = int((high+low)/2)        
        print('Is your secret number', str(number) + '?')
        ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    elif ans == 'l':
        low = number
        number = int((high+low)/2)
        print('Is your secret number', str(number) + '?')
        ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    else:
        print('Sorry, I did not understand your input.')
        print('Is your secret number', str(number) + '?')
        ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
print('Game over. Your secret number was:', str(number))