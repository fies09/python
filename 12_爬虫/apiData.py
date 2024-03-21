#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/10/13 15:14
# @Author     : fany
# @Project    : PyCharm
# @File       : apiData.py
# @description: apiData
import requests

url = 'https://api.example.com/endpoint'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Assuming the response is in JSON format
    print('API response data:', data)
else:
    print('Failed to retrieve data from API. Status code:', response.status_code)
