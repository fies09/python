#coding = utf-8
'''
    标题  基本数据类型False值
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
#列举布尔值为False的常见值
#0
#[]
#""
#tuple()
#dict()
#set()
#常见的数据类型中所有表示空的东西都可以称之为False
# print(bool(0))
# def func():
#     pass

# print(bool(func))   #True

class mClass(type):
    def __bool__(self):
        return False

class MyClass(metaclass=mClass):    #给了元类,那么bool()转化的时候,根据元类去判断
    def __bool__(self):     #对象在进行转化的时候,根据这个函数去判断
        return False
    pass

print(bool(MyClass))#False
print(bool(MyClass()))#调用类的对象   #False