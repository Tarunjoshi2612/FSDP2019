# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:29:12 2019

@author: Tarun Joshi
"""

import pandas as pd

churn_df = pd.read_csv("Telecom_churn.csv")
churned_df = churn_df[churn_df['churn'] == True]

plans_count = churned_df[(churned_df['international plan'] == 'yes') & (churned_df['voice mail plan'] == 'yes')].shape
plans_count = plans_count[0]
print (plans_count)    
    
call_charge = churn_df.groupby('churn')['total intl charge'].sum()
visual_1 = call_charge.plot.pie(autopct='%1.1f%%')

night_call = churned_df['total night minutes'].max()

call_analysis = churned_df.iloc[:, 7:19].sum().sort_index()
visual_2 = call_analysis.plot.bar()

non_churn_al = churn_df['account length'][churn_df['churn'] == False].max()
churn_al = churned_df['account length'].max()
if churn_al > non_churn_al:
    print('churned user have the maximum account lenght')
else:
    print('regular user have the maximum account lenght')

customer_care = churned_df['customer service calls'].value_counts()

area_popl = churn_df.groupby('area code')['international plan'].value_counts().unstack()