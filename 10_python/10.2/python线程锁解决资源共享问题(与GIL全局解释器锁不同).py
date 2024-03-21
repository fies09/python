#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/8/7 21:23
# @Author     : fany
# @Project    : PyCharm
# @File       : python线程锁解决资源共享问题(与GIL全局解释器锁不同).py
# @description:
import threading
import time

# 定义一个全局变量
g_num = 0

# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()


def sum1(num):
    global g_num
    # mutex.acquire()     # 若在此处上锁，要等下面循环执行完才会解锁，若循环时间太长，会导致另外的线程堵塞等待。
    for i in range(num):
        # 上锁，如果之前没有被上锁，那么此时上锁成功。 上锁原则：一般对产生资源竞争的代码上锁。如果上锁之前 已经被上锁了，那么此时会堵塞在这里，直到 这个锁被解开为止。
        mutex.acquire()
        g_num += 1
        # 解锁
        mutex.release()
    print("-----in test1 g_num=%d----" % g_num)


def sum2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("-----in test2 g_num=%d=----" % g_num)


def main():
    t1 = threading.Thread(target=sum1, args=(1000000,))
    t2 = threading.Thread(target=sum2, args=(1000000,))

    t1.start()
    t2.start()

    # 等待上面的2个线程执行完毕....
    time.sleep(2)

    print("-----in main Thread g_num = %d---" % g_num)


if __name__ == "__main__":
    main()