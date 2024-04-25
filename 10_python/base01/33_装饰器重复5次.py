#coding = utf-8
'''
    标题 
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
def wrapper(fn):
    def inner(*args,**kwargs):
        for i in range(5):
            ret = fn(*args,**kwargs)
        return ret
    return inner

@wrapper
def func():
    print("我要打游戏")

func()
