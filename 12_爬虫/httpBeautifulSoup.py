#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/10/13 15:08
# @Author     : fany
# @Project    : PyCharm
# @File       : httpBeautifulSoup.py
# @description: httpBeautifulSoup
from bs4 import BeautifulSoup

html_content = '<html><body><h1>Hello, World!</h1></body></html>'
soup = BeautifulSoup(html_content, 'html.parser')

heading = soup.h1.text
print('Heading:', heading)
