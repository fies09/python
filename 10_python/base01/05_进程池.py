#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/13 00:49
# @Author     : fany
# @Project    : PyCharm
# @File       : 05_进程池.py
# @description:
'''
进程的创建和删除是需要消耗计算机资源的，如果有大量任务需要多进程完成，则可能需要频繁的创建删除进程，这会给计算机带来较多的资源消耗。进程池的出现解决了这个问题，它的原理是创建适当的进程放入进程池，等待待处理的事件，当处理完事件后进程不会销毁，仍然在进程池中等待处理其他事件，直到事件全部处理完毕，进程退出。 进程的复用降低了资源的消耗。
'''
import time, os

from multiprocessing import Pool


def worker(msg):
    start_time = time.time()
    print(F"{msg}开始执行，进程pid为{os.getpid()}")
    time.sleep(1)
    end_time = time.time()
    print(F"{msg}执行完毕，耗时{end_time - start_time}")


def main():
    po = Pool(3)    # 定义进程池最大进程数为3
    for i in range(10):
        # 每次循环会用空闲出的子进程调用目标
        po.apply_async(worker, args=(i,))   # 若调用的函数报错，进程池中不会打印报错信息

    po.close()  # 关闭进程池，关闭后，不再接收新的目标
    po.join()   # 等待进程池中所有子进程执行完，必须放在close()之后。若没有join()操作，主进程执行完后直接关闭
    print("--end--")


if __name__ == "__main__":
    main()