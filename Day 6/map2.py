# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:09:52 2019

@author: Tarun Joshi
"""

names = ['Mary', 'Isla', 'Sam']
s=list (map(lambda x :hash(x) ,names))
print(s)