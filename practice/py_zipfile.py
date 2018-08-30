# -*- coding: UTF-8 -*-

'''

    zipfile模块用来做zip格式编码的压缩和解压缩的，zipfile里有两个非常重要的class, 分别是ZipFile和ZipInfo,
    在绝大多数的情况下，我们只需要使用这两个class就可以了。
    ZipFile是主要的类，用来创建和读取zip文件而ZipInfo是存储的zip文件的每个文件的信息的。


'''
import zipfile
import os


FILE_NAME = "test.zip"
FILE_NAME1 = "test1.zip"

def zip_file():

    '''
        比如要读取一个Python
        zipfile
        模块，这里假设filename是一个文件的路径:


    '''

    cur_path = os.getcwd()
    z = zipfile.ZipFile(FILE_NAME, 'r')
    for i in z.infolist():
        # file_path = os.path.join(cur_path, i.filename)
        # print file_path
        # if os.path.isfile(file_path):
        print i.filename, i.file_size, i.header_offset


    print z.namelist()  #list

    '''
        这里使用了z.infolist(), 它返回的就是压缩包内所有文件的信息，就是一个ZipInfo的列表。
        一个ZipInfo对象中包含了压缩包内一个文件的信息，其中比较常用的是filename, file_size, header_offset, 分别为文件名，文件大小，文件数据在压缩包中的偏移。
        
        其实之前的z.namelist()就是读取的ZipInfo中的filename，组成一个list返回的。
    '''

    # 从压缩包里解压缩出一个文件的方法是使用ZipFile的read方法
    # 这样就读取出z.namelist()中的第一个文件，并且输出到屏幕，当然也可以把它存储到文件。
    z = zipfile.ZipFile(FILE_NAME, 'r')
    content = z.read(z.namelist()[0])

    # with open("test.txt","w") as f:
    #     f.write(content)
    #     f.close()



    # 下面是创建zip压缩包的方法，与读取的方法其实很类似的：

    z1 = zipfile.ZipFile(FILE_NAME1, 'w')
    # 注意这里的第二个参数是w，这里的filename是压缩包的名字

    # 假设要把一个叫testdir中的文件全部添加到压缩包里（这里只添加一级子目录中的文件）
    testdir = os.path.join(cur_path,"doc")
    ## 切换到doc目录
    os.chdir(testdir)
    if os.path.isdir(testdir):
        for d in os.listdir(testdir):
            z1.write(d)
        z1.close()


    # 面的代码非常的简单。想想还有一个问题，如果我把一个test/111.txt 添加到压缩包里之后我希望在包里它放到test22/111.txt怎么办呢？
    # 其实这个就是Python ZipFile模块的write方法中第二个参数的作用了。只需要这样调用：
    # z.write("test/111.txt", "test22/111.txt")


    #解压
    os.chdir(cur_path)
    zipf = zipfile.ZipFile(FILE_NAME1)

    zipf.extractall('channel1')  # 将所有文件解压到channel1目录下


if __name__ == "__main__":
    print "zipfile--------"

    zip_file()