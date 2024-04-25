#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/8/7 21:20
# @Author     : fany
# @Project    : PyCharm
# @File       : python多线程资源竞争.py
# @description:
'''
因为多线程共享全局变量，当线程还没执行完当前任务，操作系统就自动轮流调度执行其他任务，就可能会产生资源竞争的问题。
比如下例中，执行 g_num+=1 时，会将其分成3步执行：1.取值；2.运算;3.保存运算结果，在CPU执行任务时，若刚运行1 2 步就交替执行下一个任务，再返回来保存结果，因为共享全局变量，此时运算结果可能已被重新赋值。
'''
import time
import threading

g_num = 0


def sum1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print(F"sum1：{g_num}")


def sum2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print(F"sum2：{g_num}")


def main():
    t1 = threading.Thread(target=sum1, args=(1000000,))
    t2 = threading.Thread(target=sum2, args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(2)
    print(g_num)    # 执行后，预期结果为2000000；实际不是


if __name__ == "__main__":
    main()