# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:30:56 2019

@author: Tarun Joshi
"""

#Vowels Finder

vowel=['a','e','i','o','u']
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
i=0
for x in state_name:
    while i<len(x):
        if x[i] in vowel:
            x=x.replace(x[i],"")
            i=i+1
    final_list.append(x)
print(final_list)