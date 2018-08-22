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


def rename_func():
    ''''
        Python的os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件。
        要使用这个模块，你必须先导入它，然后才可以调用相关的各种功能。
        rename()方法：
        rename()方法需要两个参数，当前的文件名和新文件名。

        语法：
        os.rename(current_file_name, new_file_name)
    '''
    # 重命名文件
    if exists(FILE_NEW_NAME):
        os.remove(FILE_NEW_NAME)

    if exists(FILE_NAME):
        os.rename(FILE_NAME, FILE_NEW_NAME)


def os_dir_func():
    dir_name = "newDirTest"
    if not exists(dir_name):
        os.mkdir(dir_name)  # 创建目录
    else:
        os.rmdir(dir_name)  # 删除目录

    # 可以用chdir()方法来改变当前的目录
    # 将当前目录改为"/home/newdir"
    # os.chdir("/home/newdir")

    # getcwd()方法显示当前的工作目录。

    cur_path = os.getcwd()
    print "当前目录1：", cur_path

    os.chdir("../")  # 改变到上级目录
    cur_path = os.getcwd()
    print "当前目录2：", cur_path

    # os.listdir(path)返回path指定的文件夹包含的文件或文件夹的名字的列表 只返回一级目录

    dir_files = os.listdir(cur_path)
    for x in dir_files:
        print x

    # 当前目录
    curDir = os.curdir
    print curDir  # (.)

    # 当前操作平台 Window是'nt' Linux/Unix是'posix'
    curOs = os.name
    print curOs


def listDir(rootDir):
    # os.path.isfile os.path.isdir ==>文件 目录
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if (os.path.isfile(pathname)):
            print pathname
        elif (os.path.isdir(pathname)):
            listDir(pathname)


def bianli_dirs():
    ''''
        方法一 : 利用函数 os.walk()
            os.walk() 会返回三元元组 (dirpath, dirnames, filenames)
            dirpath : 根路径 (字符串)
            dirnames : 路径下的所有目录名 (列表)
            filenames : 路径下的所有非目录文件名 (列表)

            其中目录名和文件名都是没有加上根路径的，所以需要完整路径时需要将目录名或文件名与根路径连接起来。

        方法二 : 利用函数 os.listdir(), os.path.isdir(), os.path.isfile()

            os.listdir() 可以列出路径下所有文件和目录名，但是不包括当前目录., 上级目录.. 以及子目录下的文件.
            os.path.isfile() 和 os.path.isdir() 判断当前路径是否为文件或目录

    '''
    cur_path = os.getcwd()
    print "当前目录1：", cur_path

    os.chdir("../")  # 改变到上级目录
    cur_path = os.getcwd()

    print "当前目录2：", cur_path

    # for dirpath, dirnames, filenames in os.walk(cur_path):
    #     for filepath in filenames:
    #         print os.path.join(dirpath, filepath)

    listDir(cur_path)


REMOVE_FILE = "copy2.txt"


def remove_file():
    if exists(REMOVE_FILE):
        # 删除文件
        os.remove(REMOVE_FILE)


def syetem_cmd():
    # 运行系统命令
    cmd = "pwd"
    os.system(cmd)


def os_path_func():
    # "获取文件大小"

    cur_path = os.getcwd()

    print  cur_path

    # os.path.isfile os.path.isdir ==>文件 目录
    file = ""
    for filename in os.listdir(cur_path):
        pathname = os.path.join(cur_path, filename)  # 连接目录和文件名或者目录 使用"\"连接
        if (os.path.isfile(pathname)):
            # 文件类型
            if file == "":
                file = pathname
            print pathname + " is file"
        elif (os.path.isdir(pathname)):
            # 文件夹类型
            print pathname + " is dir"

    # os.path.split 将path分割成目录和文件名的二元组返回
    array = os.path.split(cur_path)  # 返回一个元组：不可变化的list
    for arr in array:
        print arr

    # os.path.basename 返回文件名
    file_name = os.path.basename(file)
    print "file_name ", file_name

    # 返回文件路径
    file_path = os.path.dirname(file)
    print "file_path ", file_path

    print "文件路径+文件名：", os.path.join(file_path, file_name)


if __name__ == "__main__":

    # rename_func()

    # os_dir_func()

    # bianli_dirs()

    # remove_file()

    # syetem_cmd()

    os_path_func()