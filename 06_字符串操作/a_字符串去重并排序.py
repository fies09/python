#coding = utf-8
'''
    标题 
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
#s = 'ajldjlajfdljfddd',去重并从小到大排序输出'adfjl'  集合去重
s = 'ajldjlajfdljfddd'
se = set(s)
l = list(se)
l.sort(reverse=False)   #sort 方法无返回值
str2 = ""
print(str2.join(l))

