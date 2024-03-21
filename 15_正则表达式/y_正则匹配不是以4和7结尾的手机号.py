#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
import re
tels = ['16855827681','16855827684','16855827687','16855827683','1006']
for tel in tels:
    r = re.match('\d{10}[0-3,5-6,8-9]$',tel)
    if r:
        print(r.group())



