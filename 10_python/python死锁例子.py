#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/8/7 21:25
# @Author     : fany
# @Project    : PyCharm
# @File       : python死锁例子.py
# @description:
'''
某个线程获取锁后无法释放锁，导致其他线程无法继续执行。
避免死索办法：1、添加超时时间；2、银行家算法（让锁按预期上锁和解锁）
在线程间共享多个资源的时候，如果两个线程分别占用部分资源并且同时等待对方的资源，就会造成死锁。尽管死锁很少发生，但一旦发生就会造成应用停止响应。下面看一个死锁例子。
'''
import time
import threading


# 创建多个锁
mutexA = threading.Lock()
mutexB = threading.Lock()


def print1():
    mutexA.acquire()
    time.sleep(2)   # 等待B锁稳定
    print("打印A1")
    mutexB.acquire()
    print("打印B1")
    mutexB.release()
    mutexA.release()


def print2():
    mutexB.acquire()
    time.sleep(1)   # 等待A锁稳定
    print("打印B2")
    mutexA.acquire()
    print("打印A2")
    mutexA.release()
    mutexB.release()


def main():
    t1 = threading.Thread(target=print1)
    t2 = threading.Thread(target=print2)

    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
