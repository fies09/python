#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/8/7 21:17
# @Author     : fany
# @Project    : PyCharm
# @File       : python的多线程.py
# @description:
'''
一个进程可以有一个或多个线程
'''
import time
import threading


def say(sleep_time):
    for i in range(5):
        print(f"说{i+1}下")
        time.sleep(sleep_time)

def dance():
    for i in range(10):
        print(f"跳{i+1}下")
        time.sleep(1)

def main():
    # 创建线程对象
    # target：指定线程调用的函数名。注:等号后跟方法名不能加括号，如果加了也能执行函数但threading功能无效
    # args：指定调用函数时传递的参数。注:args是一个数组变量参数，只传一个参数时，需要在参数后面添加逗号
    t1 = threading.Thread(target=say, args=(1,))
    t2 = threading.Thread(target=dance)

    # 启动线程
    t1.start()
    t2.start()

    # 查看正在运行的线程
    while True:
        now_threading = threading.enumerate()
        print(now_threading)
        # 当子线程全部运行结束后，仅剩1个主线程
        if len(now_threading) <= 1:
            break
        time.sleep(1)


if __name__ == "__main__":
    main()