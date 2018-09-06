# -*- coding: UTF-8 -*-

'''
    python shutil模块

    主要作用与拷贝文件用的

'''

import shutil
import  os
import stat

#仅仅之拷贝权限，
def copymode(src, dst):
    """copy mode bits from src to dst"""
    if hasattr(os,'chmod'):
        st = os.stat(src)
        mode = stat.S_IMODE(st.st_mode)
        os.chmod(dst,mode)

# 仅仅拷贝内容
def copyfile(src, dst):
    shutil.copyfile(src, dst)

#权限内容都拷贝
def copy(src, dst):
    shutil.copy(src, dst)

def func1():

    #shutil.copyfileobj(文件1，文件2)：将文件1的数据覆盖copy给文件2。

    # f1 = open("test.txt", "r")
    # f2 = open("2.txt", "w")
    # shutil.copyfileobj(f1, f2)
    # f1.close()
    # f2.close()


    #shutil.copyfile(文件1，文件2)：不用打开文件，直接用文件名进行覆盖copy
    # shutil.copyfile("test.txt", "3.txt")

    #shutil.copymode(文件1，文件2)：之拷贝权限，  内容组，用户，均不变
    # copymode("test.txt", "4.txt")

    #shutil.copy(文件1，文件2)：拷贝文件和权限都进行copy。
    # copy("test.txt", "5.txt")

    #####################################
    '''
        拷贝目录 shutil.copytree
        上传目录 shutil.rmtree
        移动目录 shutil.move

    :return:
    '''
    #shutil.copytree(源目录，目标目录)：可以递归copy多个目录到指定目录下
    # 子目录也一起拷贝 目标目录跟源目录结构一样
    # shutil.copytree("doc","doc1")

    #shutil.rmtree(目标目录)：可以递归删除目录下的目录及文件。
    # shutil.rmtree("doc1")

    #shutil.move(源文件，指定路径)：递归移动一个文件。
    # shutil.move("2.txt","doc1")

    #shutil.make_archive()：可以压缩，打包文件。
    # 参数意思：压缩包文件名，压缩格式，打包路径
    shutil.make_archive("doc1", "zip", "doc1")



if __name__ == "__main__":
    print "shutil-----------"

    func1()