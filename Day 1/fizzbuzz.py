# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:34:05 2019

@author: Tarun Joshi
"""

# Fizz Buzz

i=1
while i<101:
    if i%15==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
    i=i+1