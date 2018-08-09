#_*_ coding:utf-8 _*_

import os 
import os.path 
import shutil 
import time,  datetime

sourceDirPath = "C:/Users/hexinping/Desktop/aochuang/walk/8"
targetDirPath = "C:/Users/hexinping/Desktop/aochuang1"

#把某一目录下的所有文件复制到指定目录中 目标文件不存在新建一个
def copyFiles(sourceDir,  targetDir): 
    if sourceDir.find(".svn") > 0: 
        return 
    for file in os.listdir(sourceDir): 
        sourceFile = os.path.join(sourceDir,  file) 
        targetFile = os.path.join(targetDir,  file) 
        if os.path.isfile(sourceFile): 
            if not os.path.exists(targetDir):  
                os.makedirs(targetDir)  
            if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):  
                    open(targetFile, "wb").write(open(sourceFile, "rb").read()) 
        if os.path.isdir(sourceFile): 
            First_Directory = False 
            copyFiles(sourceFile, targetFile)


copyFiles(sourceDirPath,targetDirPath)

# import string
# import random
# import datetime

# # print range(1,10)

# # print type(string.atoi('1'))

# # for x in xrange(1,10):
# # 	print random.choice([0,1,2,3,4,5,6,7,8,9])

# # d1 = datetime.datetime.strptime('2013/03/05', '%Y/%m/%d')
# # d2 = datetime.datetime.strptime('2012/03/02', '%Y/%m/%d')
# # delta = d1 - d2


# # print delta.days

# dictT = {'name':'hxp','age':22}

# print {}.fromkeys(('name','age'),('hxp',22))
