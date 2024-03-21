#coding = utf-8
'''
    标题
    @name:
    @function:
    @author: Mr.Fan
    @date:2021--  
'''
#斐波那契数列
items = int(input("请输入斐波那契数列的个数:"))
fibs = [0,1]
for i in range(items-1):
    fibs.append(fibs[-2]+fibs[-1])
print('斐波那契数列为:',fibs[1:])

#冒泡排序
def bubblesort(list):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

    return list

if __name__ == '__main__':
    #用户输入
    str = input("请输入数字(逗号隔开):")
    list = [int(i) for i in str.split(',')]
    print(bubblesort(list))
