#coding = utf-8
'''
    标题 赋值的意义
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
求结果:
kvps = {'1':1,'2':2}
theCopy = kvps
kvps['1'] = 5
sum = kvps['1'] + theCopty['1']
print(sum)
'''
kvps = {'1':1,'2':2}
theCopy = kvps  #赋值操作就是让两个变量指向同一个内存地址
kvps['1'] = 5
sum = kvps['1'] + theCopy['1']
print(sum)  #10