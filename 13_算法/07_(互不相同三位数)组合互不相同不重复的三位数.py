#coding = utf-8
'''
    标题 互不相同三位数
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
#1,2,3,4,5能组合成多少个互不相同且无重复的三位数
lst = []
nums = {1,2,3,4,5}
for i in range(100,1000):
    s =set(int(j) for j in str(i))   #256 => {2,5,1} -{1,2,3,4,5} => {}
    if not s - nums:
        # print(i)
        lst.append(s)
print(len(lst))