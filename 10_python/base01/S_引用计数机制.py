#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
简述Python中引用计数机制
'''
#python 垃圾回收主要以引用计数为主,标记清除和分代清除为辅,其中标记清除和分代清除主要是为了处理循环引发的难题

import time
class Animal(object):
    #创建完对象之后会自动被调用
    def __init__(self,name):
        print('__init__方法被调用')
        self.name = name

    def __del__(self):
        print('__del__方法被调用')
        print('%s对象马上被干掉了' % self.name)

cat = Animal('bisimao')
cat2 = cat
cat3 = cat
print(id(cat),id(cat2),id(cat3))    #输出结果是内存地址相同

del cat
del cat2
del cat3    #__del__方法只有在对象真正被删除的时候才调用,也就是cat3被删除的时候

'''
引用计数算法
当一个变量保存了对象的引用时,此对象的引用计数就会＋1
当使用del去删除变量指向的对象时,如果对象的引用计数不为1,比如3,那么此时只会让引用计数-1,即变为2,
再次调用变为1,再次调用,此时会真的把对象删除
'''
