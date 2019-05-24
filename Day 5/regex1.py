# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:08:52 2019

@author: Tarun Joshi
"""

# Regular Expression 1
     
import re

str1=input("Enter floating point number : ")
item=re.match(r"[-+]?\d*\.\d+$",str1)
if item:
    print ("True")
else:
    print ("False")
