#coding = utf-8
'''
    标题 
    @name:  
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
'''
python一个数如果恰好等于它的因子之和,这个数就称为完数,eg:6 = 1 + 2 + 3 ,编程找出1000以内的完数
'''
#因子:能够被整除的
#8:1 2 4
#6:1 2 3
for n in range(1,1000):
    n_lst = []
    for i in range(1,n):    #1 2 3 4 5 6 7
        if n % i == 0:
            n_lst.append(i)

    if sum(n_lst) == n:
        print(n,'是一个完数','因子有',n_lst)