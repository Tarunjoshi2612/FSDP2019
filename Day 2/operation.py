# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:41:38 2019

@author: Tarun Joshi
"""

#Operations Function

str=input("enter elements of list")
list1=str.split()
def add(a):
    sum=0
    for x in a:
        sum=sum+int(x)
    return sum
def mul(a):
    prod=1
    for x in a:
        prod=prod*int(x)
    return prod

print(add(list1))
print(mul(list1))