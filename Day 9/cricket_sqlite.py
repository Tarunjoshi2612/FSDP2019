# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:34:33 2019

@author: Tarun Joshi
"""

from bs4 import BeautifulSoup
import requests
import sqlite3

cricket = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(cricket).text
soup = BeautifulSoup(source,"lxml")

_table=soup.find('table', class_='table')


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
tb=_table.find('tbody')

for row in tb.findAll('tr'):
    cells = row.findAll('td')
   
    A.append(cells[0].text.strip())
    B.append(cells[1].text.strip())
    C.append(cells[2].text.strip())
    D.append(cells[3].text.strip())
    E.append(cells[4].text.strip())
    
conn = sqlite3.connect ( 'cric.db' )
c = conn.cursor()
c.execute ("""CREATE TABLE cricket6(
          position TEXT, 
          team name TEXT,
          weighted_match TEXT, 
          point TEXT,
          rating TEXT
          )""")
for i in range(0,10):
    c.execute("INSERT INTO cricket6 VALUES ('{}','{}','{}','{}','{}')".format(A[i],B[i],C[i],D[i],E[i]))
c.execute("SELECT * FROM cricket6")
print ( c.fetchall() )
