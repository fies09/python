#coding = utf-8
'''
    标题 降维
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
请尽量用简介的方法把二维数组转化为一维数组
eg:
    转换前
    lst =[[1,2,3],[4,5,6],[7,8,9]]
    转换后
    lst = [1,2,3,4,5,6,7,8,9]
'''
#列表的相加
# lst1 = [1,2,3]
# lst2 = [4,5,6]
# lst3 = lst1 + lst2
# print(lst3)

# from functools import reduce
# lst = [[1,2,3],[4,5,6],[7,8,9]]
# lst2 = list(reduce(lambda  x,y:x+y,lst))
# print(lst2)

# from itertools import chain
# lst = [[1,2,3],[4,5,6],[7,8,9]]
# lst2 = list(chain.from_iterable(lst))
# print(lst2)

lst = [[1,2,3],[4,5,6],[7,8,9]]
lst2 = sum(lst,[])
print(lst2)