#coding = utf-8
'''
    标题 filter(function,iterable)
    @name:  将可迭代对象的每个元素作为参数传递给函数,然后筛选出返回了True的元素
    @function:  判断函数
    @author: Mr.Fan
    @:return: 迭代器对象
    @iterable: 可迭代对象
    @date:2021--  
'''
'''
    filter方法求出列表所有奇数并构造新列表a=[1,2,3,4,5,6,7,8,9,10]
'''
# a=[1,2,3,4,5,6,7,8,9,10]
# b = filter(lambda x : x % 2 != 0,a)
# for i in b:
#     print(i)


a=[1,2,3,4,5,6,7,8,9,10]
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd,a)))