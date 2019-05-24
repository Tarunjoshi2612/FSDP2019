# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:35:54 2019

@author: Tarun Joshi
"""

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

states = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source = requests.get(states).text
soup = BeautifulSoup(source,"lxml")

_table=soup.find('table', class_='wikitable sortable')


A=[]
B=[]

tb=_table.find('tbody')

for row in tb.findAll('tr'):
    cells = row.findAll('td')
   
    if len(cells)==7:
        A.append(cells[1].text.strip())
        B.append(cells[4].text.strip())
list1=A[:6]
list2=B[:6]
lables=list1
sizes=list2
explode = (0.2,0,0,0,0,0)

plt.pie(sizes, explode = explode, labels=lables, autopct='%2.2f%%',shadow=True, startangle=0)
plt.axis('equal')

plt.show()
