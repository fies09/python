#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/13 00:56
# @Author     : fany
# @Project    : PyCharm
# @File       : 10_shlex使用.py
# @description:
import shlex
s = "I am Bill"
ret = shlex.split(s)
print(ret)

# 同时可以用来去除字符串中的单双引号
s = "test '1234'"
ret = shlex.split(s)
print(ret)
# 单双引号在中间也会被出掉
s = 'test "223"4'
ret = shlex.split(s)
print(ret)

# 需要注意的是，若字符串成对单双引号有空格，是不会分割的
s = 'test "2234 323"4'
ret = shlex.split(s)
print(ret)

# 需要注意的是，若字符串中的单双引号不是成对出现会报错:No closing quotation
try:
    s = 'test "2234'
    ret = shlex.split(s)
    print(ret)
except ValueError as e:
    print("出错了", e)