# -*- coding: UTF-8 -*-


'''
    题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

    程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
    (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
    (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
    (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

'''

# 返回小于某个数内的所有质数列表
def getZhiShuList(num):

    import time
    start = time.clock()
    i = num
    # 创建一个空list

    r = list()

    # 添加元素2
    r.append(2)

    # 从3开始挨个筛选
    for a in range(3, i):
        b = False

        # 用a除以小于a的质数b
        for b in r:
            if a % b == 0:
                b = False
                break
            else:
                b = True
        if b == True:
            r.append(a)

    t = (time.clock() - start)
    print "time: %f" % t

    return r


def func1():

    n = int(raw_input(">:"))
    num = n
    list = getZhiShuList(n)
    list.sort() #默认从小到大排列

    k = list[0]
    print list

    t = ""
    while True:

        if k == n :
            print k
            t = t + str(k)
            break
        else:
            if n % k == 0:
                t = t + str(k) + "*"
                print k
                n /= k
            else:
                k += 1


    print "%d=%s" % (num, t)


if __name__ == "__main__":
    print "14-----------"
    func1()