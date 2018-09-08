# -*- coding: UTF-8 -*-

'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

'''

def func1():
    for i in range(1, 1001):
        sum = 0
        for j in range(1, i):
            if i % j == 0:
                sum += j
        if sum == i:
            print(i)

def getWanShu(num):
    sum = 1  # 1要加上，所以默认赋值为1
    for i in range(2, num):  # 因子不包括本身，
        if num % i == 0:
            sum += i
    if sum == num:
        return num

def func2():

    result = []
    for num in range(2, 1000):
        test = getWanShu(num)
        if test:   # 去掉空值
            result.append(test)
    print "完数有：", result

if __name__ == "__main__":
    print "19-----------"
    # func1()
    func2()