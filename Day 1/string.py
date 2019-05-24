# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:59:45 2019

@author: Tarun Joshi
"""

# String Handling

name=input("enter first name and last name")
index=name.find(" ")
print(name[index+1:]+" "+name[:index+1])