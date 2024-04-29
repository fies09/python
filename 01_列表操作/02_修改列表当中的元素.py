#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Time : 2024/3/25 22:44
# @Author : fany
# @Project : PyCharm
# @File : 02_修改列表当中的元素.py
# @description:
# l = [2,3,4,5,4,6]
# # l[3] = 10
# # print(l)
# if 4 in l:
#     print(l.index(4))

def find_first_duplicate_index(lst):
    seen = set()
    for index, value in enumerate(lst):
        if value in seen:
            return index
        seen.add(value)
    return -1  # 如果没有找到重复值，返回-1或其他标志值

# 示例
lst = [1, 2, 3, 2, 5, 6]
index = find_first_duplicate_index(lst)
print(f"第一个重复值的索引是: {index}")

