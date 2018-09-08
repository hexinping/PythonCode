# -*- coding: UTF-8 -*-

'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

'''


def func1():

    n = 1
    a = 2.0
    b = 1.0
    sum = 0
    pre_a = 0
    pre_b = 0
    while n <= 20:

        if pre_a != 0 and pre_b != 0:
            a = pre_a + pre_b
            b = pre_a
        num = a/b
        sum += num
        pre_a = a
        pre_b = b
        n += 1
    print "sum=%f" % sum



def func2():
    a = 2.0
    b = 1.0
    s = 0
    for n in range(1, 21):
        s += a / b
        ## 重新赋值a b
        t = a
        a = a + b
        b = t
    print s


    # for i in range(1, n+1):
    #     num = a/b
    #     sum += num


if __name__ == "__main__":
    print '24---------'
    func1()