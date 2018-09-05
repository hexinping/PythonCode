# -*- coding: UTF-8 -*-

'''
题目：将一个列表的数据复制到另一个列表中。

程序分析：使用列表[:]。

'''




def func1():

    a = [1, 2, 3]
    b = a[:]
    print b

def func2():

    import copy
    a = [1, 2, 3]
    b = copy.copy(a)
    print b


def func3():
    l = [1, 2, 3, 4, 5]
    p = []
    for i in range(len(l)):
        p.append(l[i])
    print p


def func4():


    import copy
    a = [1, 2, 3, 4, 5]
    b = ["A", "B", a]
    # 浅拷贝
    c = b[:]
    print c

    a[0] = 11
    print  c   #['A', 'B', [11, 2, 3, 4, 5]] 此时a变化c跟着变化


    # 深拷贝
    c = copy.deepcopy(b)
    print c

    a[0] = 112
    print c   #['A', 'B', [11, 2, 3, 4, 5]] 此时c中数据不受a影响





if __name__ == "__main__":
    print "07------------"
    func1()
    func2()
    func3()
    func4()