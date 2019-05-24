# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:07:54 2019

@author: Tarun Joshi
"""

import pandas as pd

dataset = pd.read_csv('Automobile.csv')
dataset["price"] = dataset["price"].astype(str)
dataset["price"][dataset["price"] == '  '] = 'nan'
dataset["price"] = dataset["price"].astype(float)
dataset["price"] = dataset["price"].fillna(dataset["price"].mean())
price_numpy_array = dataset["price"].values

print ( "Minimum Price is {0}".format( dataset["price"].min() ) )
print ( "Maximum Price is {0}".format( dataset["price"].max() ) )
print ( "Average Price is {0}".format( round( dataset["price"].mean(), 2 ) ) )
print ( "Standard Deviation of Price is {0}".format( round( dataset["price"].std(), 2 ) ) )