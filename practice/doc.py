# #_*_ coding:utf-8 _*_

from sys import argv

# from sys import argv 从sys模块中导入argv模块

"""
    命令行参数是字符串吗?
    是的，就算你在命令行输入数字，你也需要用 int() 把它先转成数字，和在 raw_input() 里一样。

"""
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