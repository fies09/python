#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/10/13 15:06
# @Author     : fany
# @Project    : PyCharm
# @File       : httpRequests.py
# @description: httpRequests
import requests

url = 'https://example.com'
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print('Failed to retrieve the page. Status code:', response.status_code)
