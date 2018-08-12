# #_*_ coding:utf-8 _*_

from sys import argv

# from sys import argv 从sys模块中导入argv模块

def print_argvs():

    # 参数解包 一一赋予值 : 脚本本身 参数1 参数2 参数3
    first, second, three, four = argv

    first = raw_input("脚本名字：")
    print "first is ", first

    second = raw_input("参数1：")
    print "second is ", second

    three = raw_input("参数2：")
    print "three is ", three

    four = raw_input("参数3：")
    print "four is ", four

if __name__ == "__main__":

    print_argvs()