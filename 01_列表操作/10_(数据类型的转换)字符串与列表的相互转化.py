#coding = utf-8
'''
    标题 数据类型转换
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
#如何实现'1,2,3'变成['1','2','3']
#如何实现['1','2','3']变成[1,2,3]
s = '1,2,3'
#split() 字符串的切割
lst = s.split(",")
print(lst)

#用列表推导式搞定第二问
lst2 = [int(item) for item in lst]
print(lst2)