# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:34:05 2019

@author: Tarun Joshi
"""

# SSA Analysis
    
import pandas as pd

df1=pd.DataFrame(columns = ['Name', 'Sex', 'Number','Year'])
for i in range(1880,2018):
    filename="yob"+str(i)+".txt"
    df2 = pd.read_csv(filename,header=None)
    df2.columns = ['Name', 'Sex', 'Number']
    df2['Year']=i
    df2 = df2.sort_values(by=['Number'], ascending=False)
    df1=pd.concat([df1, df2])
    
print("Top 5 male baby name in 2010\n",df1[(df1["Sex"] == "M") & (df1["Year"] == 2010)].head(5))
print("Top 5 male baby name in 2010\n",df1[(df1["Sex"] == "F") & (df1["Year"] == 2010)].head(5))

df=df1.groupby(['Year', 'Sex'])['Number'].aggregate('sum').unstack()
df.plot()    