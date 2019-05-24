# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:18:44 2019

@author: Tarun Joshi
"""

import re
with open('simpsons_phone_book.txt') as fh:
    for line in fh:
        if re.search(r"J.*Neu",line):
            print(line)