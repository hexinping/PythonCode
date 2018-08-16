# #_*_ coding:utf-8 _*_


def printLog():
    print "hello world"
    print 'sprite'
    print 'texture'
    print 'i am sad today'
    print '笑书神侠倚碧鸳'


def operator():
    '''
        • + plus  加号
        • - minus  减号
        • / slash  斜杠
        • * asterisk  星号
        • % percent  百分号
        • < less-than  小于号
        • > greater-than  大于号
        • <= less-than-equal  小于等于号
        • >= greater-than-equal  大于等于号

        print "I will now count my chickens:"
        print "Hens", 25 + 30 / 6
        print "Roosters", 100 - 25 * 3 % 4
        print "Now I will count the eggs:"
        print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
        print "Is it true that 3 + 2 < 5 - 7?"
        print 3 + 2 < 5 - 7
        print "What is 3 + 2?", 3 + 2
        print "What is 5 - 7?", 5 - 7
        print "Oh, that's why it's False."
        print "How about some more."
        print "Is it greater?", 5 > -2
        print "Is it greater or equal?", 5 >= -2
        print "Is it less or equal?", 5 <= -2


    '''
    print 'i will now vount chickens'
    print 'hens', 25 + 30 / 6
    print 'is is greater?', 5 > -2

    print 'test float', 2.0/5  #浮点运算会保留小数位
    print 'test float', 2 / 5  #整数运算不会保留小数位  python3.0就好了



# 计算一个数的阶乘
def factorial(num):

    if num < 2 :
        return 1
    return num * factorial(num -1)


def calulate(count):
    '''

        计算1+2！+3！+4！+……+10！

    '''
    sum = 0
    for num in range(1, count):
        sum = sum + factorial(num)
    return sum

if  __name__ == "__main__":

    printLog()

    operator()

    sum = calulate(10)
    print "sum====",sum


