#coding = utf-8
'''
    标题 循环删除问题
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
阅读以下代码,并写出程序的输出结果
alist = [2,4,5,6,7]
for var in alist:
    if var % 2 == 0:
        alist.remove(var)

print(alsit)
'''
alist = [2,4,5,6,7]
for var in alist[:]:
    if var % 2 == 0:
        alist.remove(var)

print(alist)