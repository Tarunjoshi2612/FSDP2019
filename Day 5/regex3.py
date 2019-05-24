# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:49:12 2019

@author: Tarun Joshi
"""
import re

str1=input("enter credit card number")
list1=str1.split("")
if len(list1)!=16:
    print("invalid")
else:
    for item in list1:
        if item==', ' or '_':
            print("invalid")
        else :
            item2=re.match(r'^[456](\d{15}|\d{3}-(\d{4}-){2}\d{4})$',str1)
            if item:
                print ("valid")
            else:
                print ("invalid")
            
            
