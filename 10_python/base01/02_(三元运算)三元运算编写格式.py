#coding = utf-8
'''
    标题 三元运算
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
#格式:() if () else ()
#计算a和b中比较大的值
a = 10
b = 20
if a > b:
    c = a
else:
    c = b
print(c)

#值1 if 条件 else 值2
#条件为True,结果值1,否则值2
c = a if a > b else b
print(c)