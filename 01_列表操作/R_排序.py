#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
43,list = [2,3,4,5,9,6],从小到大排序,不许用sort,输出[2,3,4,5,6,9]
'''
#利用main()方法求出最小值,原列表删除最小值,新列表加入最小值,递归调用获取最下值的函数,反复操作(重新写)
l = [2,3,4,5,9,6]
new_l = []
def pal(l):
    a = min(l)
    l.remove(a)
    new_l.append(a)
    if len(l)>0:
        pal(l)
        return new_l
pal(l)
print(new_l)