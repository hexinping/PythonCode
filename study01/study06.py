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


def argv_raw_input():

    script, user_name = argv
    prompt = '> '

    print "Hi %s, I'm the %s script." % (user_name, script)

    print "I'd like to ask you a few questions."

    print "Do you like me %s?" % user_name
    likes = raw_input(prompt)
    print "Where do you live %s?" % user_name
    lives = raw_input(prompt)
    print "What kind of computer do you have?"
    computer = raw_input(prompt)

    # 定义多行字符串 """。。。。"""
    print """
    Alright, so you said %r about liking me.
    You live in %r.  Not sure where that is.
    And you have a %r computer.  Nice.
    """ % (likes, lives, computer)


if __name__ == "__main__":

    # print_argvs()

    argv_raw_input()