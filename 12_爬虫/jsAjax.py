#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/10/13 15:16
# @Author     : fany
# @Project    : PyCharm
# @File       : jsAjax.py
# @description: 解析Ajax请求
import requests

url = 'https://example.com/api'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Assuming the response is in JSON format
    print('API response data:', data)
else:
    print('Failed to retrieve data from API. Status code:', response.status_code)
