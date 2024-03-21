#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/1/12 22:15
# @Author     : fany
# @Project    : PyCharm
# @File       : 02_字符串处理.py
# @description:
# python3中,strip匹配两测所有不符合条件的字符(括号内指定字符串中的每个字符)
from pprint import pprint
strs = 'abbacabb'
pprint(strs.strip('ab'))

# 统计字符在字符串中出现的次数 string.count('字符')
# s = '一花一木一世界'
# print(s.count('一'))
# # 将string中的old_str替换为new_str,  string.replace('要替换的字符', '替换后的')
# print(s.replace('一', '三'))
# # lstrip():清除左空格,rstrip(): 清除右空格 , strip():清除空格
# s = "  一花一木一世界  "
# print(len(s))
# ss = s.strip()
# print(len(ss))
# # 判断是否少于x个字符,如果少于,用其他的补充,如果没有,默认空格 ljust左对齐.rjust右对齐
# s1 = "sss"
# s2 = "xxxxx"
# print(s1.ljust(8, "-"))
# print(s2.ljust(8, "-"))
# 右对齐
s1 = "假如"
s2 = "给我三天光明"
print(s1.rjust(8, "-"))
print(s2.rjust(8, "-"))
# 因为我们用的不是等宽字体，所以上面两行数据右边没有对齐，如果有强迫症，可以使用中文的空白字符串
s1 = "假如"
s2 = "给我三天光明"
print(s1.rjust(8, '　'))
print(s2.rjust(8, '　'))
# 居中对齐
s1 = "假如"
s2 = "给我三天光明"
print(s1.center(8, '-'))
print(s2.center(8, '-'))