# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:02:26 2019

@author: Tarun Joshi
"""

# Pallindromic Integer

str1=input("Enter a space separated list of integers")
list1=str1.split(" ")
list2=[]
for i in list1:
    if int(i)>0:
        list2.append("true")
    else:
        list2.append("false")
if all(list2):
    s=any(list (map(lambda x: True if x==x[::-1] else False, list1)))
    print(s)
else:
    print("false")