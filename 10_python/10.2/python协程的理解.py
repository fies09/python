#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/8/7 21:27
# @Author     : fany
# @Project    : PyCharm
# @File       : python协程的理解.py
# @description:
'''
在执行函数A时可以随时中断去执行函数B,然后终端函数B继续执行函数A,协程只有一个函数执行
协程库及使用方法
gevent常用方法：
gevent.spawn() 创建一个普通的Greenlet对象并切换
gevent.spawn_later(seconds=3) 延时创建一个普通的Greenlet对象并切换
gevent.spawn_raw() 创建的协程对象属于一个组
gevent.getcurrent() 返回当前正在执行的greenlet
gevent.joinall(jobs) 将协程任务添加到事件循环，接收一个任务列表
gevent.wait() 可以替代join函数等待循环结束，也可以传入协程对象列表
gevent.kill() 杀死一个协程
gevent.killall() 杀死一个协程列表里的所有协程
monkey.patch_all() 非常重要，会自动将python的一些标准模块替换成gevent框架
'''
# import gevent
#
#
# def task(n):
#     for i in range(n):
#         print(gevent.getcurrent(), i)
#
#
# if __name__ == '__main__':
#     g1 = gevent.spawn(task, 3)
#     g2 = gevent.spawn(task, 3)
#     g3 = gevent.spawn(task, 3)
#
#     g1.join()
#     g2.join()
#     g3.join()
# 可以看到3个greenlet是依次运行而不是交替运行。要让greenlet交替运行，可以通过gevent.sleep()交出控制权：


'''
当然在实际的代码里，我们不会用gevent.sleep()去切换协程，而是在执行到IO操作时gevent会自动完成，所以gevent需要将Python自带的一些标准库的运行方式由阻塞式调用变为协作式运行。这一过程在启动时通过monkey patch完成：
'''
# import time
# import gevent
# from gevent import monkey
# # 猴子补丁，会自动将python的一些标准模块替换成gevent框架。慎用，它创造了“隐式的副作用”，如果出现问题 它很多时候是极难调试的。
# monkey.patch_all()  # 注意：若导出的模块函数不会被替换，比如from time import sleep，sleep不会被替换
#
#
# def task(n):
#     for i in range(n):
#         print(gevent.getcurrent(), i)
#         time.sleep(1)   # 会被gevent自动替换为gevent.sleep()
#
#
# if __name__ == '__main__':
#     g1 = gevent.spawn(task, 3)
#     g2 = gevent.spawn(task, 3)
#     g3 = gevent.spawn(task, 3)
#
#     g1.join()
#     g2.join()
#     g3.join()

'''
上面的流程看起来比较繁琐，可以使用 gevent.joinall() 方法简化流程：
'''

import time
import gevent
from gevent import monkey
# 猴子补丁，会自动将python的一些标准模块替换成gevent框架。慎用，它创造了“隐式的副作用”，如果出现问题 它很多时候是极难调试的。
monkey.patch_all()  # 注意：若导出的模块函数不会被替换，比如from time import sleep，sleep不会被替换


def task(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(1)   # 会被gevent自动替换为gevent.sleep()


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(task, 4),
        gevent.spawn(task, 4),
        gevent.spawn(task, 4),
    ])