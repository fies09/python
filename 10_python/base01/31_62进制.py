#coding = utf-8
'''
    标题 
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
写一个base62encode函数,计算62进制
即0123456789ABCD...Zabcd...z(10个数字,26个大写字母.26个小写字母)

base62encode(1) = 1
base62encode(61) = z
base62encode(62) = 10
'''
def base62encode(n):
    lst = []
    s = '0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    #s = '0123456789ABCDEF'       16进制
    while n > 0:
        y = n % 62      #%16
        lst.append(s[y])
        n = n // 62     #//16


    return ''.join(lst[::-1])

print(base62encode(1))
print(base62encode(61))
print(base62encode(62))
print(base62encode(185))
