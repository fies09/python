#coding = utf-8
'''
    标题 
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
写装饰器,限制函数被执行频率,如10s一次
'''
import time
def wrapper(fn):
    start = 0   #上一次访问时间
    def inner(*args,**kwargs):
        nonlocal start
        now = time.time()
        if now - start > 10:
            ret = fn(*args,**kwargs)
            start = now
            return ret
        else:
            print("对不起,您访问的过于频繁,请于{10-int(now-start)之后}")
    return inner

@wrapper
def fun():
    print('我要打游戏')

fun()

