#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2022/12/9 18:19
# @Author     : fany
# @Project    : PyCharm
# @File       : 04_合并两个有序列表.py
# @description:
# 尾递归
def _recursion_meege_sort2(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_meege_sort2(l1, l2, tmp)

def recursion_meege_sort2(l1, l2):
    return _recursion_meege_sort2(l1, l2, [])

# 循环算法
def loop_merge_sort(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
    tmp.append(l1)
    tmp.append(l2)
    return tmp