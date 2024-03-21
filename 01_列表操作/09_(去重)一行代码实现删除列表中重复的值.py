#coding = utf-8
'''
    标题 去重
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
#一行代码实现删除列表中重复的值
lst = ['广坤','赵四','刘能','广坤']
#集合去重
#借助,set集合,数据是不重复的
s = set(lst)
print(list(s))