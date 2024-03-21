#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
举例说明zip函数()的用法
'''
#zip在运算时,会以一个或多个序列(可迭代对象)作为参数,返回一个元组的列表,同时将这些序列中对应的元素匹配
#当两个参数的长度不同时,zip会以最短序列长度为基准截取,获得元组
a = [1,2]
b = [3,4]
res = [i for i in zip(a,b)]
print(res)  #[(1, 3), (2, 4)]

a = 'ab'
b = 'xyz'
res = [i for i in zip(a,b)]
print(res)  #[('a', 'x'), ('b', 'y')]


'''
zip用法
'''
x = ['a','b','c','d','e']
y = [1,2,3,4,5]
z = [i for i in zip(x,y)]
print(z)