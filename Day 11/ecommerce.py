# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:03:44 2019

@author: Tarun Joshi
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
plt.hist(incomes, bins=50)
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))
incomes=np.append(incomes,[1000000000000])
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))