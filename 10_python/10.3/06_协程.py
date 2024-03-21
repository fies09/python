#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/13 00:50
# @Author     : fany
# @Project    : PyCharm
# @File       : 06_协程.py
# @description:
'''
协程，又称微线程。协程的作用是在执行函数A时可以随时中断去执行函数B，然后中断函数B继续执行函数A（可以自由切换）。但这一过程并不是函数调用，这一整个过程看似像多线程，然而协程只有一个线程执行。

协程的优势：

执行效率极高，因为子程序切换（函数）不是线程切换，由程序自身控制，没有切换线程的开销。所以与多线程相比，线程的数量越多，协程性能的优势越明显。
不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在控制共享资源时也不需要加锁，因此执行效率高很多。
'''
'''
gevent
gevent是第三方库，通过 greenlet 实现 coroutine，创建、调度的开销比 线程(thread) 还小，因此程序内部的 执行流 效率高。

其基本思想是：当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。

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
    # g1.join()
    # g2.join()
    # g3.join()



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