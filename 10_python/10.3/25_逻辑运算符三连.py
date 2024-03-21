#coding = utf-8
'''
    标题 
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
1 or 2 和1 and 2输出是什么?为什么?
1 < (2==2)和1 < 2 == 2结果是什么?为什么?
'''
# print(1 or 2)#or 左右两边有一个是真,结果就是真
# print(0 and 2)#  and 必须左右都是真,结果才能是真

#顺序 () => not => and => or
# print(1 > (2 == 2))
print(1 < 2 and 2==2)