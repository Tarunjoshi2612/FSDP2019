# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:55:23 2019

@author: Tarun Joshi
"""

#Weighted Score Calculator

#marks scored in assignments
A1=int(input("enter marks obtained in assignments out of 100")) 
A2=int(input())
A3=int(input())
#marks scored in tests
E1=int(input("enter marks obtained in tests out of 100"))
E2=int(input())
#weighted score
WS=((A1+A2+A3)*0.1+(E1+E2)*0.35)
print(WS)