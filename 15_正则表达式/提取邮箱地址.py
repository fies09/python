#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/10/11 10:44
# @Author     : fany
# @Project    : PyCharm
# @File       : 提取邮箱地址.py
# @description: 提取邮箱地址
import re

text = 'Hello, my email is example@example.com'
pattern = r'[\w\.-]+@[\w\.-]+'
emails = re.findall(pattern, text)
print('Emails:', emails)
