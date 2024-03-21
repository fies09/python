#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
    两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
'''
a = [1,5,7,9]
b = [2,2,6,8]
print(a)
a.extend(b)
a.sort()
print(a)