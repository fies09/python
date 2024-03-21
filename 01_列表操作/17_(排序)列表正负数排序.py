#coding = utf-8
'''
    标题 排序
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
将列表按下列规则排序,补全代码
1,正数在前,复数在后
2,正数从小到大
3,复数从大到小
eg:
    排序前:[7,-8,5,4,0,-2,-5]
    排序后:[0,4,5,7,-2,-5,-8]
请补全代码:
    sorted(lst,key=lambda x:_____)
'''
#     (0,7) (1,8)  (0,5) (0,4)  0  1  1
lst = [7,   -8,    5,    4,     0,-2,-5]
res = sorted(lst,key=lambda x:(x<0,abs(x)))
print(res)
