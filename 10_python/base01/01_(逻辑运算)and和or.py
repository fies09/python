#coding = utf-8
'''
    标题 逻辑运算
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
考点:
    逻辑运算符
    and 并且
    or  或者
    not 非
    
    运算顺序:   ()=> not => and => or
    
    a or b:
    如果a 表示False,那么结果就是b
    如果a 表示True,那么结果就是a
    
    a and b:
    如果a表示True,那么结果就是b
    如果a表示False,结果就是a
'''
#0是False
v1 = 1 or 3 #1
v2 = 1 and 3    #3
v3 = 0 and 2 and 1  #0
v4 = 0 and 2 or 1   #1
v5 = 0 and 2 or 1 or 4  #1
v6 = 0 or False and 1   #False
print(v1,v2,v3,v4,v5,v6)
