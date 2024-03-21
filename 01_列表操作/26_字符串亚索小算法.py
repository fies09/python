#coding = utf-8
'''
    标题 
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
    把字符串aaabbcccd压缩成a3b2c3d1这种形式
f: a
count :3
result = a3b2c3d1
'''
s = 'aaabbcccd'
f = s[0]
count = 1
result = ''
for i in range(1,len(s)):   #循环字符串的索引
    if s[i] == f:
        count += 1
    else:
        #把f和count记录
        result += f + str(count)
        #更换f和count
        f = s[i]
        count = 1
result += f + str(count)
print(result)

