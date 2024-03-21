#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/13 01:00
# @Author     : fany
# @Project    : PyCharm
# @File       : 02_字符串排序.py
# @description:
while 1:
    try:
        # 输入字符串
        line = input()
        # 定义一个空字符串, 一个空字典
        alpha, other = '', {}
        # index和i分别是字符串line的索引和值
        for index, i in enumerate(line):
            # 判断所有字符是否都是字母
            if i.isalpha():
                # 将所有字符放到空字符串中
                alpha += i
            else:
                # 如果所有字符不是字母类型,将非字母类型放到字典中
                other[index] = i
        # 将新的字符串按照字母大小进行排序
        new = sorted(alpha, key=lambda x: x.upper())
        # 将非字符串放到排序后的列表中进行排序打印
        for key, value in other.items():
            new.insert(key, value)
        print(''.join(new))
    except:
        break
