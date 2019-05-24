# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:45:29 2019

@author: Tarun Joshi
"""
# Replacing of Characters

str="RESTART"
first=str.find('R') #find the index of 1st 'R' and store it in first
print(str[:first+1]+ str[first+1:].replace("R","$")) #print string as it is till (first+1)
#print rest of the string till end replacing each "R" with"$"