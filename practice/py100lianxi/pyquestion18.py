# -*- coding: UTF-8 -*-

'''
    题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

    程序分析：关键是计算出每一项的值。

'''

def get_die_num(num, count):
    sum = 0
    count -= 1
    while count >= 0:
        n = num * 10 **count
        sum += n
        count -= 1
    return sum

def func1():

    num = int(raw_input(">"))
    count  = 5
    sum = 0

    s = ""
    while count > 0:
        n = get_die_num(num,count)
        if s == "":
            s += str(n)
        else:
            s = s + "+" + str(n)
        sum += n
        count -= 1

    print "%d = %s" % (sum, s)


def func2():
    Tn = 0
    Sn = []
    n = int(raw_input('n = '))
    a = int(raw_input('a = '))
    for count in range(n):
        Tn = Tn + a
        a = a * 10
        Sn.append(Tn)
        print Tn

    Sn = reduce(lambda x, y: x + y, Sn)
    print "计算和为：", Sn

if __name__ == "__main__":
    print "18--------"
    # func1()
    func2()