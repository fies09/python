#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2022/12/12 15:34
# @Author     : fany
# @Project    : PyCharm
# @File       : 14_删除一个list里面的重复元素.py
# @description:
l = [1,1,2,3,4,5,4]
print(list(set(l)))

d = {}
for i in l:
    d[i] = 1
mylist = list(d.keys())
print(mylist)

my_list = [1, 2, 2, 3, 4, 4, 5]

# 使用集合去重并保持原始顺序
my_list = list(dict.fromkeys(my_list))

print(my_list)

