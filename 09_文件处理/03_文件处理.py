#!/usr/bin/env python
# -*- coding : utf-8 -*-
# 文件打开
file = open('a.txt', 'r', encoding='utf-8')
# print(file)
# 读取文件全部内容
# print(file.read())
# 读取文件中最多size个字符, 读取前size个内容
# print(file.read(20))
# 读取并返回一行
# print(file.readline())
# 读取返回所有行的列表
# print(file.readlines())

# 写入文件 (写入（'w'）、追加（'a'）或读写（'r+'）)
# write()或writelines()方法
file = open('a.txt', 'w', encoding='utf-8')
file.write('hello world')
file.close()

# 关闭文件
file.close()

# with关键字的作用,自动关闭文件
with open('a.txt', 'r', encoding='utf-8') as file:
    print(file.read())













