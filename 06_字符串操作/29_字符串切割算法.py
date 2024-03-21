#coding = utf-8
'''
    标题 
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
对于一个非空字符串,判断其是否可以有一个子字符串重复多次组成,字符串只包含小写字母且长度不超过10000
示例1:
    输入:'abab'
    输出:True ,输入可由ab重复两次组成
示例2:
    输入:'abcabcabc'
    输出:True ,输入可由abc重复3次组成
示例3:
    输入:'aba'
    输出:False
'''
s = input('>>>:')

for i in range(2,len(s)//2 +1 ):    #范围
    lst =  s.split(s[:i])   #切割,用谁切,就会损失谁
    lst = [item for item in lst if item != '']
    if not lst:
        print(f'True,输入可由{s[:i]}重复{len(s)/i}次组成')
        break
else:
    print('False')
#abcabcabc #split() 用谁切,就会损失谁