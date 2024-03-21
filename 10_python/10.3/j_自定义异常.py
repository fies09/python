#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
#自定义异常
#1,步骤1,创建自定异常类
class Age(ValueError):
    pass

age = int(input('age:'))
if 0 < age < 150:
    print(age)
else:
    #抛出异常
    raise Age("年龄必须要在0~150之间")

#2
# class XueException(Exception):
#     def __init__(self,msg):
#         self.msg = msg
# try:
#     raise XueException("my error")
# except XueException as e:
#     print(e)