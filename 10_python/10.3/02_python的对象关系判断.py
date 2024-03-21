#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/12 21:20
# @Author     : fany
# @Project    : PyCharm
# @File       : 02_python的对象关系判断.py
# @description:
# 【字符串】类型判断
print(isinstance("s", str))

# 【浮点数】类型判断
print(isinstance(3.14, float))

# 【整数型】类型判断
print(isinstance(66, int))

# 【布尔】类型判断
print(isinstance(True, bool))

# 【列表】类型判断
print(isinstance(["a", 1, True], list))

# 【元组】类型判断
print(isinstance(("b", 1), tuple))

# 【字典】类型判断
print(isinstance({"a": 1, "b": 2}, dict))

# 【集合】类型判断
print(isinstance({"a", "b"}, set))

# 函数/方法类型判断
import types
def func():
    pass

class A(object):

    @classmethod
    def class_method(cls):
        pass

    def method(self):
        pass

print('*' * 50)
print(isinstance(func, types.FunctionType))     # 函数判断
print(isinstance(A.class_method, types.MethodType))     # 方法判断
print(isinstance(A().method, types.MethodType))         # 方法判断
print(isinstance(A.class_method, types.FunctionType))   # 函数的判断类型不能用于方法的判断
print(isinstance(A().method, types.FunctionType))       # 函数的判断类型不能用于方法的判断

# class类型判断(类)
class A:
    pass

class B(object):
    pass

print('#' * 50)
print(type(A))
print(type(B))
print(isinstance(A, type))
print(isinstance(B, type))

# 判断对象是否是一个已知类或子类的实例化对象。
class A(object):
    pass

class B(A):
    pass

class C(object):
    pass


a = A()
b = B()
c = C()
print('#' * 50)
print(isinstance(a, A))
print(isinstance(b, A))
print(isinstance(C, A))


# 判断对象是否是一个已知类或是该已知类的子类
# 此类判断需用 issubclass方法。
class A(object):
    pass

class B(A):
    pass

class C(B):
    pass

class D(object):
    pass

print('*' * 50)
print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(D, A))


