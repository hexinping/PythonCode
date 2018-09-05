# -*- coding: UTF-8 -*-

'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....

'''


def func1():
    f1 = 1
    f2 = 1
    for i in range(1, 22):
        print '%12ld %12ld' % (f1, f2),
        if (i % 3) == 0:
            print ''
        f1 = f1 + f2
        f2 = f1 + f2


def func2():
    # 递归做，非常慢。计算n=36就要大概七八秒吧
    def fib(n):
        if n == 1 or n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print fib(36)

def func3():
    n = int(raw_input("第几个月： "))
    # 斐波那契数列的通项公式  **幂 - 返回x的y次幂
    f = (1 / (5 ** 0.5)) * (((1 + (5 ** 0.5)) / 2) ** n - ((1 - (5 ** 0.5)) / 2) ** n)
    print "第%d个月：共%d只" % (n, f)

if __name__ == "__main__":
    print "11------------"
    # func1()
    # func2()
    func3()