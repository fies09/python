#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
log日志中,我们需要用时间戳记录error,warning等发生时间,请用datetime模块打印当前时间戳"2021-02-24 23:21:54"
'''
#时间戳,
import datetime
a = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "星期" + str(datetime.datetime.now().isoweekday())
b = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(a,b)