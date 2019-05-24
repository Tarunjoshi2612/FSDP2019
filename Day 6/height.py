# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:28:18 2019

@author: Tarun Joshi
"""

from functools import reduce

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
list1=list(filter(lambda x: 'height' in x, people))
list2=list(map(lambda x:x['height'] , list1))
sum1=reduce(lambda x,y : x + y,list2)
average=sum1/(len(list2))
print(average)