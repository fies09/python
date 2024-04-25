#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/13 00:55
# @Author     : fany
# @Project    : PyCharm
# @File       : 09_单例模式.py
# @description:
# 单例模型的原理就是对__new__方法进行重写，而重写new方法的代码非常固定，唯一值得注意的是一定要 return super().__new__(cls)，否则python解释器得不到分配了空间的对象引用，就不会调用对象的初始化方法。


class MusicPlayer:

    # 记录第一个被创建对象的引用
    __instance = None

    # 重写__new__ 方法创建单例模型
    # 说明：__new__方法是object基类提供的一种静态方法。
    # 作用：1、为对象分配空间；2、返回对象引用
    def __new__(cls, *args, **kwargs):
        # 1、判断类属性是否为空引用,若为空则为对象分配空间
        if cls.__instance is None:
            print("这里还能执行其他只初始化一次的操作")
            cls.__instance = super().__new__(cls)
        # 返回对象引用
        return cls.__instance

    def __init__(self, name):
        self.name = name
        print(f"{self.name}播放器初始化完成")


# 创建多个对象
player1 = MusicPlayer("千千")
player2 = MusicPlayer("万万")
print(player1 is player2)