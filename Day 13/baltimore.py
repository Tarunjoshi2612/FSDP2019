# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:10:10 2019

@author: Tarun Joshi
"""

# Baltimore City Analysis

import pandas as pd
import numpy as np

df = pd.read_csv('Baltimore_City_Employee_Salaries_FY2014.csv',header=0)

df['AnnualSalary'] = df['AnnualSalary'].astype(float)


grouped = df.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])

output = df.sort_values(['AnnualSalary'],ascending=0)
print (str(output.iloc[0,0])+" get the highest salary")

grouped = df.groupby(['JobTitle'])
sorted(grouped)

df['JobTitle'].value_counts()[0:10].plot('bar')

aggregated.sort_values(['sum'],ascending=0,inplace=True)
print (str(aggregated.index[0])+" job title spends the most")

aggregated['sum'][0:10].plot('bar')

agency_name_id = df[['Agency','AgencyID']]
agency_name_id.drop_duplicates(inplace=True)

df['GrossPay'].isnull().sum()