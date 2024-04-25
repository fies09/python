#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/8/7 19:47
# @Author     : fany
# @Project    : PyCharm
# @File       : python的多进程.py
# @description:
'''
进程,程序执行的一次过程,是临时,有生命周期,动态产生,动态消亡的
进程可以并发执行,是系统进行资源分配和调度的一个独立单位,由程序,数据和进程控制块三部分组成
'''
# 多进程
import multiprocessing
import time

def run1(sleep_time):
    while True:
        print('-- 1 --')
        time.sleep(sleep_time)

def run2(sleep_time):
    print('-- 2 --')
    time.sleep(sleep_time)

def main():
    # 创建进程对象
    # target: 指定线程调用的函数名. 注:等号后跟方法名不能加括号，如果加了也能执行函数但threading功能无效
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