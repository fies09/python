'''
实现步骤:
 1, 确定递归结束条件
 2, 编写递归函数,该函数中需要调用自身来实现递归
 3, 调用递归函数
'''
# 计算斐波那契数列第n项
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))