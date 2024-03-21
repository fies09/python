#coding = utf-8
'''
    标题 extend
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
有一个多层嵌套列表A = [1,2,[3,4,["434",...]]],请写一段代码遍历A中的每个元素并打印出来
extend()
'''
# lst1 = [1,2,3]
# lst2 = [4,5,6]
# lst1.extend(lst2)
# print(lst1)   #[1, 2, 3, 4, 5, 6]

A = [1,2,[3,4,["434",...]]]
#extend,将两个列表内的元素放到一个列表中
for item in A:
    if type(item) == list:
        A.extend(item)
    else:
        print(item)
