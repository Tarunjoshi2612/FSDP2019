# -*- coding: utf-8 -*-
"""
Created on Sun May 19 23:48:14 2019

@author: Tarun Joshi
"""
# book shop 1

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]

min_order = 100

order_summary = list(map(lambda x: (x[0], round(x[2] * x[3],2)), orders))
print(order_summary)

total= list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), order_summary))
print(total)

