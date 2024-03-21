#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
    列表推导式求列表所有奇数并构造新列表a= [1,2,3,4,5,6,7,8,9,10]
'''
a = [1,2,3,4,5,6,7,8,9,10]
res = [i for i in a if i % 2 == 1]
print(res)