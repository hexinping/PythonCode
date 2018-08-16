# #_*_ coding:utf-8 _*_

# 行尾的冒号的作用是告诉 Python 接下来你要 创建一个新的代码区段。这根你创建函数时的冒号是一个道理

def logic_fuhao():

    print 'python 逻辑术语'

    print '''
        • and与
        • or或
        • not非
        • != (not equal) 不等于 
        • ==(equal)等于
        • >=(greater-than-equal)大于等于 
        • <=(less-than-equal)小于等于
        • True真
        • False假
    '''


def logic_if():

    '''

    if xxx:

    else:

    ---------

    if xxx:
    elif xxx:
    else:

    '''




    people = 10
    cats = 30
    dogs = 15

    if people < cats :
        print "people < cats"
    else:
        print "people >= cats"


    if cats < dogs:
        print "cats < dogs"
    elif dogs < people:
        print "dogs < people"


def logic_if1():

    door = int(raw_input(">"))

    if door == 1 :
        print "door == 1"
    elif door == 2:
        print "door == 2"
    else:
        print "door is others"



if __name__ == "__main__":

    logic_fuhao()

    logic_if()
    logic_if1()

