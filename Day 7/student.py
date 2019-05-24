# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:39:11 2019

@author: Tarun Joshi
"""
import json

student =[{
        "First Name": "Yash",
        "Last Name": "Gupta",
        "Photo": "abc.com",
        "Department":"I.T.",
        "Contact Details":[
        {"Mobileno":987654321,
        "email": "abc@gmail.com"
        }]},

        {"First Name": "Sunil",
        "Last Name": "Jangir",
        "Photo": "abc.com",
        "Department":"I.T.",
        "Contact Details":[
        {"Mobileno":987654321,
        "email": "abc@gmail.com"
        }]}
        ]
file2= json.dumps(student)
with open("st.json","w") as st:
    json.dump(file2,st)
