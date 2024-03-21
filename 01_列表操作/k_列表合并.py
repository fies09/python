#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
    [[1,2],[3,4],[5,6]]一行代码展开该列表,得出[1,2,3,4,5,6]
'''
a = [[1,2],[3,4],[5,6]]
x = [j for i in a for j in i]
print(x)