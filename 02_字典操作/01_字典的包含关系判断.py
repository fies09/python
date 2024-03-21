#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/12 21:19
# @Author     : fany
# @Project    : PyCharm
# @File       : 01_字典的包含关系判断.py
# @description:
a = {"a": 1, "b": 2, "c": 3, "d": 4}
b = {"b": 2, "c": 3}
c = {"a": 2, "b": 2}
print(a.items())
print(b.items() <= a.items())
print(c.items() <= a.items())