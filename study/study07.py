# #_*_ coding:utf-8 _*_

#pydoc xxx 查看一个对象的属性和方法

from sys import argv
from os.path import exists


config_path = "config/"
#file_name = "study07.txt"

def file_opt():

    script, file_name = argv

    file = open(config_path+ file_name)
    print "Here's you file %s" % file_name
    print file.read()

    file.close()



def file_opt1():

    '''
        • close–关闭文件。跟你编辑器的文件->保存..一个意思。
        • read – 读取文件内容。你可以把结果赋给一个变量。
        • readline–读取文本文件中的一行。
        • truncate–清空文件，请小心使用该命令。
        • write(stuff) – 将 stuff 写入文件。


        最重要的是 + 修饰符，写法就是 'w+', 'r+', 'a+' ——这样的话文件将以同时读写的方式打 开，而对于文件位置的使用也有些不同。
        如果只写 open(filename) 那就使用 'r' 模式打开的吗? 是的，这是 open() 函数的默认工作方式。

    '''

    script, file_name = argv
    file = open(config_path + file_name,"w") # w模式打开会自动删除原有内容 a+追加内容

    file.truncate()  #这一句其实可以不要
    line1 = raw_input("Line1:")
    line2 = raw_input("Line2:")
    line3 = raw_input("Line3:")

    file.write(line1 + "\n")
    file.write(line2 + "\n")
    file.write(line3 + "\n")

    file.close()


def file_opt2():

    to_file = config_path + "copy.txt"
    script, from_file = argv

    print "Copying from %s to %s" % (from_file, to_file)
    in_file = open(config_path + from_file)
    indata = in_file.read()

    print "The input file is %d bytes long" % len(indata)

    print "Does the output file exist? %r" % exists(to_file)

    print "Ready, hit RETURN to continue, CTRL-C to abort."

    # raw_input()


    out_file = open(to_file, 'a+')

    out_file.write(indata)


    print "Alright, all done."

    out_file.close()
    in_file.close()

if __name__ == "__main__":

    # file_opt()
    # file_opt1()
    file_opt2()