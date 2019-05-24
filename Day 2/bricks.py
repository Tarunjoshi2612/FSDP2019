# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:41:55 2019

@author: Tarun Joshi
"""

#Bricks
i=0
sum=0
str=input("enter number of small bricks,number of large bricks and target length")
list1=str.split()
list1=[int(x) for x in list1]
while i<3:
    if i==0:
        a=int(list1[0:1])
        sum=a*1
    elif i==1:
        sum=sum+int(list1[1:2])*5
    else:
        length=int(list1[2:3])
if sum>=length:
    print("true")
else:
    print("false")