#coding = utf-8
'''
    标题 is和==
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
#is和==的区别
'''
is判断的是内存地址
==判断的是值
'''
# lst1 = [1,2,3]
# lst2 = [1,2,3]
# print(lst1 is lst2) #False
# print(lst1 == lst2) #True

s1 = "你好啊"
s2 = "你好啊"

print(s1 == s2) #True
print(s1 is s2) #True