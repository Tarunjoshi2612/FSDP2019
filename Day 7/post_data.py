# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:47:56 2019

@author: Tarun Joshi
"""

import requests

host = "http://httpbin.org/post"
data = {"firstname":"dev","language":"English"}
response = requests.post(host,data)
print(response.content)