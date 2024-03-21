#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/10/13 15:12
# @Author     : fany
# @Project    : PyCharm
# @File       : httpRe.py
# @description: httpRe
import re

text = 'Hello, my email is example@example.com'
pattern = r'[\w\.-]+@[\w\.-]+'
emails = re.findall(pattern, text)
print('Emails:', emails)
