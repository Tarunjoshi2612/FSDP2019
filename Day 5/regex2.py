# -*- coding: utf-8 -*-
"""
Created on Mon May 20 00:13:41 2019

@author: Tarun Joshi
"""
# Regular Expression 2

import re

email_address=input("Enter your email address")
item=re.findall(r"[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,4}\b$",email_address)
print(item)