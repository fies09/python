#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/8/3 12:03
# @Author     : fany
# @Project    : PyCharm
# @File       : python作用域,全局及局部变量.py
# @description:
'''
在python中,函数会创建自己的作用域,当在函数内部访问某个变量时,函数会在自己的作用域中寻找,
自定义的全局变量均在python内建的globals()函数中,以字典形式保存,而locals()函数返回的是函数内部本地作用域中的变量名称字典
https://www.cnblogs.com/testlearn/p/12669239.html
变量的生命周期,global是()全局,local()是局部,,局部变量的生命周期在当前函数内部有效,函数退出变量的生命周期结束
在函数外部不能使用函数内部定义的局部变量
p

'''

def b():
    e = 2
    print(locals())

class C:
    def __init__(self):
        pass

print(globals())
b()