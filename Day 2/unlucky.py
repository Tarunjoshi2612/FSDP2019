# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:35:53 2019

@author: Tarun Joshi
"""
#unlucky13

flag=0
sum=0
str=input("enter elements of list")
list1=str.split()
for x in list1:
    if int(x)==13:
        flag=1
        continue
    elif flag==1:
        flag=0
        continue
    else :
        sum=sum+int(x)
print(sum)