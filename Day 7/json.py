# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:49:37 2019

@author: Tarun Joshi
"""

# JSON Parser

import requests

city=input("Enter city")
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="+city
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
#print (url)
response = requests.get(url)
#print(response.content)
jsondata = response.json()
print(jsondata["coord"])
print(jsondata["weather"][0]["description"])
print(jsondata["wind"]["speed"])
print(jsondata["sys"]["sunrise"])
print(jsondata["sys"]["sunset"])