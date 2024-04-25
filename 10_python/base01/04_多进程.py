#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/13 00:48
# @Author     : fany
# @Project    : PyCharm
# @File       : 04_多进程.py
# @description:
'''
进程是一个具有一定独立功能的程序在一个数据集上的一次动态执行的过程，是操作系统进行资源分配和调度的一个独立单位，是应用程序运行的载体。进程是一种抽象的概念，从来没有统一的标准定义。进程一般由程序、数据集合和进程控制块三部分组成。程序用于描述进程要完成的功能，是控制进程执行的指令集；数据集合是程序在执行时所需要的数据和工作区；程序控制块包含进程的描述信息和控制信息是进程存在的唯一标志。

进程具有的特征：
动态性：进程是程序的一次执行过程，是临时的，有生命期的，是动态产生，动态消亡的。
并发性：任何进程都可以同其他进程一起并发执行。
独立性：进程是系统进行资源分配和调度的一个独立单位。
结构性：进程由程序、数据和进程控制块三部分组成。

实现多进程
'''
import multiprocessing
import time


def run1(sleep_time):
    while True:
        print("-- 1 --")
        time.sleep(sleep_time)


def run2(sleep_time):
    while True:
        print("-- 2 --")
        time.sleep(sleep_time)


def main():
    # 创建进程对象。
    # target：指定线程调用的函数名。注:等号后跟方法名不能加括号，如果加了也能执行函数但threading功能无效
    # args：指定调用函数时传递的参数。注:args是一个数组变量参数，只传一个参数时，需要在参数后面添加逗号
    p1 = multiprocessing.Process(target=run1, args=(1,))
    p2 = multiprocessing.Process(target=run2, args=(1,))

    # 启用子进程
    p1.start()
    p2.start()

    # join方法等待子进程执行结束
    p1.join()
    p2.join()
    print("子进程结束")


if __name__ == "__main__":
    main()