#coding = utf-8
'''
    标题 交并集
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--
'''
'''
给定两个List,A,B,请用python找出A,B中相同的元素,A,B中不同的元素
'''
A = [1,2,3]
B = [2,3,4]

#所有和交并集相关操作都去找set集合
a = set(A)
b = set(B)
print(a & b)#交集,相同的元素
print(a ^ b)#合集,不同的元素
print(a | b)#并集,所有元素
print(a - b)#差集,A或B