# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:42:22 2019

@author: Tarun Joshi
"""

# pallindromic integer
i=0
flag=0
str=input("enter elements of list")
list1=str.split()
for x in list1:
    if int(x)<=0:
        break
    elif x[::1]==x[::-1] : 
        print("true")
        flag=1
        break
    else:
        continue
if flag==0:
    print("false")
        
        
        