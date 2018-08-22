# -*- coding: UTF-8 -*-

'''
    python IO 操作

'''
import os
from os.path import exists

'''
    读取键盘输入
    
    Python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘。如下：
    
    raw_input
    input
'''

FILE_NAME = "copy.txt"
FILE_NEW_NAME = "copy.png"

def raw_input_and_input():

    a = raw_input("raw_input > ")  #默认都返回字符串
    print a
    # b = input("input > ")
    # print b

def open_func():

    try:

        fo = open(FILE_NAME,"a+")  # a+模式打开文件指针默认在内容末尾处
        print "文件名: ", fo.name
        print "是否已关闭 : ", fo.closed
        print "访问模式 : ", fo.mode
        print "末尾是否强制加空格 : ", fo.softspace

        index = fo.tell()
        print "文件指针当前位置：", index

        fo.seek(0,0)  # 把指针再次重新定位到文件开头
        # content = fo.read()   #读取全部内容
        # print "文件内容\n", content

        #以行的形式读取文件内容

        #1
        # line = fo.readline()
        # while line:
        #     print line
        #     line = fo.readline()


        #2
        lines = fo.readlines() #以列表形式返回
        for line in lines:
            print line

        #3
        # for line in open("copy1.txt"):
        #     print line


        # fo.write("adasddf\n")

        fo.close()
    except IOError:
        print "Error: 没有找到文件或读取文件失败"



if __name__ == "__main__":

    # raw_input_and_input()
    open_func()
