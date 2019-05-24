# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:02:53 2019

@author: Tarun Joshi
"""
import json

faculty =[{
        "First Name": "Yash",
        "Last Name": "Gupta",
        "Photo": "abc.com",
        "Department":"I.T.",
        "Research Areas":["ML","C++"],
        "Contact Details":[
        {"Mobileno":987654321,
        "email": "abc@gmail.com"
        }]},

        {"First Name": "Sunil",
        "Last Name": "Jangir",
        "Photo": "abc.com",
        "Department":"I.T.",
        "Research Areas":["computer networking","linux"],
        "Contact Details":[
        {"Mobileno":987654321,
        "email": "abc@gmail.com"
        }]}
        ]
file2= json.dumps(faculty)
with open("fac.json","w") as f:
    json.dump(file2,f)