#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/13 01:01
# @Author     : fany
# @Project    : PyCharm
# @File       : 11_协程例子.py
# @description:
# 协程例子
import time

def consumer(): # 有yield,是一个生成器
    r = ""
    while True:
        n = yield r #程序暂停.等待next()信号
        #if  not n:
        #   return
        print('consumer <--%s...'%n)
        time.sleep(1)
        r = '200 ok'

def producer(c):
    next(c) #激活生成器
    n = 0
    while n < 5:
        n = n + 1
        print('produer-->%s..' % n)


        cr = c.send(n)  # 向生成器发送数据

        print('consumer return :', cr)


    c.close()  # 生产过程结束，关闭生成器


if __name__ == '__main__':
    c = consumer()
    producer(c)