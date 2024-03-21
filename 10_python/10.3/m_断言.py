#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
# python中断言方法举例
# assert()方法,断言成功,程序继续执行,断言失败,程序报错
class A(object):
    def __init__(self,name):
        self.name = name

a = A("xue")
assert type(a.name) is str
print(a.name)