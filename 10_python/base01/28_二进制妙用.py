#coding = utf-8
'''
    标题 
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
输入一个字符串,输出该字符串中字符的所有组合
例如:
    输入:1,2,3
    输出:1,2,3,12,13,23,123(组合数,不考虑顺序,所以12和21是等价的)
'''
#1, 2, 3
# 0 0 1 = 3         1
# 0 1 0 = 2         2
# 0 1 1 = 23        3
# 1 0 0 = 1         4
# 1 0 1 = 13        5
# 1 1 0 = 12        6
# 1 1 1 = 123       7
# for i in range(1,2**3):
#     print(i)    #format(i,'03b')3位长度二进制

s = '1,2,3'
lst = s.split(',')
big_result = []
for i in range(1,2**len(lst)):
    ss = format(i,f'0{len(lst)}b')  #格式化成定长的二进制

    #映射关系,把所有1位置的数据保存
    result = []
    for j in range(len(ss)):
        if ss[j] == '1':
            result.append(lst[j])
    big_result.append(int(''.join(result)))

big_result.sort()
print(big_result)
