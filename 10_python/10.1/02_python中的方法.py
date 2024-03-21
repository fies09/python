#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/6/24 23:51
# @Author     : fany
# @Project    : PyCharm
# @File       : 02_python中的方法.py
# @description:
class A(object):
    # 构造函数
    def __init__(self, title1):
        self.title = title1
        print(self.title)


    # 实例函数
    def foo(self, title2):
        print(title2)


    # 静态函数
    @staticmethod
    def static_foo():
        print("静态方法")


    # 类方法
    @classmethod
    def cls_foo(cls):
        cls.foo(a, '类函数调用实例函数')
        print('类方法')
