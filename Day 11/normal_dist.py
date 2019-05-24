# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:32:56 2019

@author: Tarun Joshi
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(150.0, 20.0, 1000)
plt.hist(incomes, bins=100)
print("Standard Deviation ",np.std(incomes))
print("Varience ",np.var(incomes))