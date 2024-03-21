#coding = utf-8
'''
    标题 深浅拷贝
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
    a = [1,2,3,[4,5],6]
    b = a   #没有拷贝
    c = copy.copy(a)
    d = copy.deepcopy(a)
    
    b.append(10)
    c[3].append(11)
    d[3].append(12)
    请问a,b,c,d的值为:???
'''
# a,b = [1,2,3,[4,5],6,10]
# c = [1,2,3,[4,5,11],6]
# d = [1,2,3,[4,5,12],6]
import copy

a = [1, 2, 3, [4, 5], 6]
b = a  # 没有拷贝
c = copy.copy(a)
d = copy.deepcopy(a)

b.append(10)
c[3].append(11)
d[3].append(12)
print(a)
print(b)
print(c)
print(d)