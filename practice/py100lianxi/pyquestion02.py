# -*- coding: UTF-8 -*-


'''

    题目：企业发放的奖金根据利润提成。
    利润(I)
        低于或等于10万元时，奖金可提10%；
        利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
        20万到40万之间时，高于20万元的部分，可提成5%；
        40万到60万之间时高于40万元的部分，可提成3%；
        60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，

    从键盘输入当月利润I，求应发放奖金总数？

    程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。

'''




def func1(value):

    single = 100000
    list = [single, 2 *single, 4 *single, 6*single, 10*single]
    rate = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
    reward = 0
    if value <= list[0]:
        return value * rate[0]

    if value > list[4]:
        reward = func1(list[4])
        reward += (value - list[4]) *rate[5]
        return reward

    count = 5
    for i in range(count):
        if i != 0:
            if i < 5:
                num1 = list[i-1]
                num2 = list[i]
                if value > num1 and value <= num2:
                    add = value - num1
                    reward = func1(num1)
                    reward += add * rate[i]
                    return reward


def func2():
    i = int(raw_input('净利润:'))
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for idx in range(0, 6):
        if i > arr[idx]:
            r += (i - arr[idx]) * rat[idx]
            print (i - arr[idx]) * rat[idx]
            i = arr[idx]
    print r


if __name__ == "__main__":
    print '02---------------'
    I = raw_input("请输入利润:")
    I = int(I)

    reward = func1(I)

    print "输入的利润是：%d, 奖金是: %d" % (I, reward)

    func2()