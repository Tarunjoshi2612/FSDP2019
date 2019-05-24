# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:00:53 2019

@author: Tarun Joshi
"""

import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
s=list (map(lambda x : random.choice(code_names) , names))
print(s)