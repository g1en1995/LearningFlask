# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:25:10 2021

@author: gcferna2
"""

import requests 
# import json

BASE = "http://127.0.0.1:5000/"


response = requests.put(BASE + "video/4", {"name": "glen4", "likes" : 40000, "views": 100000})
print(response.json())

input()

response = requests.patch(BASE + "video/1",{"views" : 10000})
print(response.json())

input()
response = requests.get(BASE + "video/0")
print(response.json())
response = requests.get(BASE + "video/1")
print(response.json())
response = requests.get(BASE + "video/2")
print(response.json())
response = requests.get(BASE + "video/3")
print(response.json())
