# -*- coding: UTF-8 -*-

'''
题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。

'''

from math import sqrt

def func1():

    h = 0
    leap = 1

    for m in range(101, 201):
        k = int(sqrt(m+1))
        for i in range(2, k+1):
            if m % i == 0:
                leap = 0  # 不是素数
                break

        if leap == 1:
            print '%-4d' % m
            h += 1
            if h % 10 == 0:
                print ''

        leap = 1

    print 'The total is %d' % h


def func2():
    l = []
    for i in range(101, 200):
        for j in range(2, i - 1):
            if i % j == 0:
                break
        else:
            l.append(i)

    print(l)

    print("总数为：%d" % len(l))

def func3():
    l = []
    for x in range(101, 201):
        l.append(x)
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                l.pop() #素数抛出
                break

    n = len(l)
    print l

    print '总数为：', n

if __name__ == "__main__":
    print "12------------"
    func1()
    func2()
    func3()
