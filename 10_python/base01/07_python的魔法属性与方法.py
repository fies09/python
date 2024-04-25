#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/13 00:50
# @Author     : fany
# @Project    : PyCharm
# @File       : 07_python的魔法属性与方法.py
# @description:
# __doc__  获取类或方法的描述信息
class Foo:
    """ 类对象__doc__的属性值"""

    def func(self):
        """ 类方法的__doc__属性值 """
        pass


foo = Foo()

print("类对象的__doc__：", Foo.__doc__)
print("实例对象的__doc__：", foo.__doc__)
print("实例对象方法的__doc__：", foo.func.__doc__)

'''
__moudle__
获取操作的所属模块，当模块在当前执行文件中时，显示__main__
'''
class Foo:
    """ 类对象__doc__的属性值"""

    def func(self):
        """ 类方法的__doc__属性值 """
        pass


foo = Foo()

print("类对象的__module__：", Foo.__module__)
print("实例对象的__module__：", foo.__module__)
print("实例对象方法的__module__：", foo.func.__module__)

# __class__
# 获取操作对象的源对象。多用于通过实例对象反向获取类对象
class Foo:
    """ 类对象__doc__的属性值"""

    def func(self):
        """ 类方法的__doc__属性值 """
        pass

    @classmethod
    def cls_func(cls):
        print("cls方法被调用")


foo = Foo()

print("类对象的源引用为Type元类：", Foo.__class__)
print("实例对象的源引用为Foo类对象：", foo.__class__)
print(Foo)

# __name__
# 获取类或方法的名称
class Foo:
    """ 类对象__doc__的属性值"""

    def func(self):
        """ 类方法的__doc__属性值 """
        pass


foo = Foo()
print("类对象的__name__：", Foo.__name__)
print("实例对象方法的__name__：", foo.func.__name__)


# __dict__
# 获取类或对象中的所有属性
class Province(object):
    country = 'China'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print('func')


# 获取类的属性，即：类属性、方法
print(Province.__dict__)
# 输出：{'__dict__': <attribute '__dict__' of 'Province' objects>, '__module__': '__main__', 'country': 'China', '__doc__': None, '__weakref__': <attribute '__weakref__' of 'Province' objects>, 'func': <function Province.func at 0x101897950>, '__init__': <function Province.__init__ at 0x1018978c8>}

obj1 = Province('山东', 10000)
print(obj1.__dict__)
# 获取 对象obj1 的属性
# 输出：{'count': 10000, 'name': '山东'}

obj2 = Province('山西', 20000)
print(obj2.__dict__)
# 获取 对象obj1 的属性
# 输出：{'count': 20000, 'name': '山西'}


'''
魔法方法 
__new__()
为对象分配内存空间，同时还返回对象的引用，在__init__()之前被调用

__init__ ()
初始化实例对象属性的方法，创建实例对象时被调用。

__init__方法中定义的实例属性如果指向的是方法(包括被 property装饰的方法)，在实例化时，会立即执行指向的方法，并将return值赋值给实例属性。当实例属性被多次调用时，也不会去执行指向的方法。

注意：利用该特效可以解决一次赋值多次使用的高耗时场景
__new__()
为对象分配内存空间，同时还返回对象的引用，在__init__()之前被调用

__init__ ()
初始化实例对象属性的方法，创建实例对象时被调用。

__init__方法中定义的实例属性如果指向的是方法(包括被 property装饰的方法)，在实例化时，会立即执行指向的方法，并将return值赋值给实例属性。当实例属性被多次调用时，也不会去执行指向的方法。

注意：利用该特效可以解决一次赋值多次使用的高耗时场景'''

class Demo:

    def __init__(self):
        self.excel_info = self.mock_read_excel()
        print("实例化完成")

    def mock_read_excel(self):
        print("读取文件")
        return "excel数据"

    def mock_use_1(self):
        return self.excel_info

    def mock_use_2(self):
        return self.excel_info

    def mock_use_3(self):
        return self.excel_info


if __name__ == '__main__':
    demo = Demo()
    demo.mock_use_1()
    demo.mock_use_2()
    demo.mock_use_3()

# __del__()
# 当对象在内存中被释放时被调用
# 注：此方法一般无须定义，因为Python是一门高级语言，程序员在使用时无需关心内存的分配和释放，因为此工作都是交给Python解释器来执行，所以，__del__的调用是由解释器在进行垃圾回收时自动触发执行的。
class Foo:
    def __del__(self):
        pass

'''
__call__()
对象后面加括号，触发执行

注：__init__方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
__call__()
'''
class Foo:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('__call__')


obj = Foo()  # 执行 __init__
obj()  # 执行 __call__

'''
__str__ ()
如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值。                        
'''
class Foo:
    def __str__(self):
        return 'laowang'


obj = Foo()
print(obj)
# 输出：laowang

'''
__getitem__()，__setitem__(),__delitem__()
用于索引操作，如字典。以上分别表示获取、设置、删除数据
'''
# -*- coding:utf-8 -*-

class Foo(object):

    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()

result = obj['k1']      # 自动触发执行 __getitem__
obj['k2'] = 'laowang'   # 自动触发执行 __setitem__
del obj['k1']           # 自动触发执行 __delitem__

'''
__setattr__()、__getattr__（）
__setattr__()：定义属性时被调用。包括外部和内部

__getattr__()：如果类中不定义该方法，在获取不存在的实例属性时会报 AttributeError；如果定义了该方法，当获取未被定义的属性时执行该方法，如果成功获取到属性则不执行该方法。
'''
class Province(object):

    def __init__(self):
        self.v = "test"     # 在内部，每一次定义实例属性都会调用 __setattr__ 方法
        a = self.s          # 在内部，每一次获取实例属性但属性不存在时调用 __getattr__ 方法
        print("a变量的值为 " + a)
        b = self.v
        print("b变量的值为 " + b)

    def __setattr__(self, key, value):
        print("定义实例属性时被调用")
        super(Province, self).__setattr__(key, value)

    def __getattr__(self, item):
        print("当获取未被定义的属性时执行该方法，如果获取到属性则不调用该方法")
        return "null"


print("===================实例化")
t = Province()

print("===================外部设置实例属性")
setattr(t, "c", "test1234")
t.d = "test2234"

print("===================外部获取实例属性")
print(t.v)
print(getattr(t, "d"))
print(t.ssss)   # 获取不存在的属性
print(getattr(t, "fffff"))  # 获取不存在的属性


'''
__iter__()
让一个对象变得可以迭代

__next__()
定义一个迭代器，让其能够通过next（迭代对象的迭代器）对一个可迭代对象进行迭代

__enter__(),__exit__()
用于定义上下文管理器
'''