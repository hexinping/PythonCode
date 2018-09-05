# -*- coding: UTF-8 -*-

'''
    题目：斐波那契数列。

    程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

    在数学上，费波那契数列是以递归的方法来定义：

    F0 = 0     (n=0)
    F1 = 1    (n=1)
    Fn = F[n-1]+ F[n-2](n=>2)

'''

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

# 使用递归
def fib1(n):
    if n==1 or n==2:
        return 1
    return fib1(n-1)+fib1(n-2)


#输出指定个数的斐波那契数列
def fib2(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs




def func1():
    # 输出了第10个斐波那契数列
    print fib(10)

    print fib1(10)

    # 输出前 10 个斐波那契数列
    print fib2(10)

if __name__ == "__main__":
    print "06-------------"
    func1()