#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
35,a = "张明 98分",用re.sub,将98替换为100
'''
import re
a = "张明 98分"
b = re.sub("[0-9]+",'100',a)
print(b)