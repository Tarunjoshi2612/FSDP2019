# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:47:20 2019

@author: Tarun Joshi
"""

import numpy as np
import random
from scipy import stats

array=np.random.randint(5,15,40)
print(array)
print("Most frequent value is: ", stats.mode(array)[0])
