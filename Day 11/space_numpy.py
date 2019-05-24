# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:09:48 2019

@author: Tarun Joshi
"""

import numpy as np

str1=input("enter 9 values")
list1=str1.split()
x = np.array(list1)
x = x.reshape(3,3)
print (x)