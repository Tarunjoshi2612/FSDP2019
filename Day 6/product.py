# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:00:51 2019

@author: Tarun Joshi
"""
from functools import reduce

str1=input("Enter list of integers")
list1=str1.split(" ")
list2=list(filter(lambda x: int(x)%2==0, list1))
prod=reduce(lambda x,y : int(x) * int(y),list2)
print("product is",prod)