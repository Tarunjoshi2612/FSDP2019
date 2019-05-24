# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:09:50 2019

@author: Tarun Joshi
"""

# Weeks

str1=input("enter day")
tup1=str1.split(",")
tup2=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
for x in tup2:
    if x in tup1:
        continue
    else:
        tup1.append(x)
print (tuple(tup1))