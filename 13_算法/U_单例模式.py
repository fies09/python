#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
写一个单例模式
因为创建对象时__new__方法执行,并必须return返回实例化出来的对象所cls_instance是否存在.不存在的话就创建对象,存在的话就返回该对象,来保证只有一个实例对象存在(单列),打印ID,值一样,说明对象同一个
'''
#实例化一个单例
class Singleton(object):
    __instance = None
    def __new__(cls, age,name ):
        #如果表属性__instance的值为None
        #那么就创建一个对象,并且赋值为这个对象的引用.保证下次调用这个方法
        #能够知道之前已经创建过了对象了,这样就保证了只有一个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

a = Singleton(18,"dongGe")
b = Singleton(8,"dongGe")

print(id(a))
print(id(b))

#给a指向的对象添加一个属性
a.age = 19
#获取b指向的对象的age属性
print(b.age)