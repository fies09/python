#coding = utf-8
'''
    标题 一个元素的元组
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
#a = [1,2,3]
#b = [(1),(2),(3)]
#c = [(1,),(2,),(3,),]
#问a,b,c有什么区别
a = (1) #()默认情况下表示的是运算的优先级(1+2)*3
print(type(a))

#如果Python中的元组值存储一个数据,那么元组最后一个元素后面必须跟上逗号
b = (1,)
print(type(b))