#coding = utf-8
'''
    标题 
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
一行代码通过filter和lambda函数输出以下列表索引为奇数对应的元素
list_a = [12,213,22,2,2,2,22,2,2,2,32]
'''
#[213,2,2,2,2]
list_a = [12,213,22,2,2,2,22,2,2,2,32]

# print(list(filter(lambda x: x[0] % 2 == 1, ((i, list_a[i]) for i in range(len(list_a))))))
print([y[1] for y in filter(lambda x: x[0] % 2 == 1, ((i, list_a[i]) for i in range(len(list_a))))])
print([list_a[y] for y in filter(lambda x: x % 2 == 1, (i for i in range(len(list_a))))])