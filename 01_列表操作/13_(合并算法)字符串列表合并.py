#coding = utf-8
'''
    标题 合并算法
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
有两个字符串列表a和b,每个字符串都是由逗号分隔的一些字符

a = [
    'a,1',
    'b,3,22',
    'c,3,4'
]
b = [
    'a,2',
    'b,1',
    'd,2'
]

按每个字符串的第一个值,合并a和b到c
c = [
    'a,1,2',
    'b,3,22,1',
    'c,3,4',
    'd,2'
]
'''
a = [
    'a,1',
    'b,3,22',
    'c,3,4'
]
b = [
    'a,2',
    'b,1',
    'd,2'
]

for b_i in range(len(b)): #b_i是b中元素的索引

    for a_i in range(len(a)):   #a_i是a中元素的索引
        if b[b_i][0] == a[a_i][0]:
            a[a_i] += b[b_i][1:]    #让a中的a_i元素拼接上b中的剩余的内容
            break
    else:   #b中的元素不在a中出现,此时没有经过break
        a.append(b[b_i])

print(a)

#while...else...