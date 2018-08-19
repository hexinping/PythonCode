# #_*_ coding:utf-8 _*_



def for_func1():

    print "for 循环"

    #使用列表

    hairs = ['brown', 'blue', 'red']
    eyes = ['blue', 'green', 'black']
    weights = [1,2,3,4]
    elements = range(0, 6)

    '''
        1 for x in xxx
        2 for x in range(min,max,step)
        
    '''


    for x in hairs:
        print "hair is %s" % x


    # x从0开始，x < 6，step默认为1   range(min,max) => [min, max -1]
    #range()函数会从第一个数到最后一个，但不包含最后一个数字
    for x in range(5,10):
        print "weight is %d" % x
        weights.append(x)

    for x in weights:
        print "append weight is %d" % x

    for x in elements:
        print "element is %d" % x


def while_fun():

#for-loop 只能对一些东西的集合进行循环， while-loop 可以对任何对象进行驯化
    i = 0
    numbers = []

    while i < 100:
        numbers.append(i)
        i += 1

        if i == 6 :
            paus = raw_input(">")
            break

    for x in numbers :
        print "x===%d" % x

if __name__ == "__main__":
    for_func1()
    while_fun()
