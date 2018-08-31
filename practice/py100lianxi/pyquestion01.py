# -*- coding: UTF-8 -*-

'''
    题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

    程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

'''


def func1():
    count = 0
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i != j and i != k and j != k :
                    print i,j,k
                    count += 1

    print "总共%d个" % count


def func2():
    list = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and i != k and j != k:
                    value = "%d%d%d" % (i,j,k)
                    list.append(value)

    print "总共%d个" % len(list)
    print list



def func3():
    #考虑减少冗余判断和循环，做如下优化；
    list = []
    for i in range(1, 5):
        for j in range(1, 5):
            if (j == i):
                continue
            for k in range(1, 5):
                if (k == i or k == j):
                    continue
                value = "%d%d%d" % (i, j, k)
                list.append(value)
    print "总共%d个" % len(list)
    print list

if __name__ == "__main__":
    print "01---------"
    # func1()
    # func2()
    func3()
