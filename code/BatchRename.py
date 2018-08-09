# #_*_ coding:utf-8 _*_

import sys
import os

motionNames = ["wait","walk","attack01","die","attack02","floating"]

# startKey = "heiaochuang"
# rootdir = "C:/Users/hexinping/Desktop/" + startKey

startKey = ""
rootdir =  "C:/Users/hexinping/Desktop/"
targetDir = "E:/work/M/M-Project-cpp/svn/Assets/role/" 


motionIndex = ""
montions = [0,0,0,0,0,0,0]
dirs = ["1","2","3","4","5","6","7","8"]
dirIndex = ""


def copyFiles(sourceDir, targetDir): 
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


class BatchRename():
    # '''
    # 批量重命名文件夹中的图片文件

    # '''
    def __init__(self):	
        self.preName = {}
        for parent,dirnames,filenames in os.walk(rootdir):
        	key = startKey
        	for dirname in dirnames:						#输出文件夹信息
				# print 'dirname is :' + dirname
				# montion = motions.index(dirname)
				if dirname in motionNames:
					motionIndex = motionNames.index(dirname) + 1
					montions[motionIndex] = motionIndex
					motionIndex = '%02d' % motionIndex
					
					# print 'dirname is ' + dirname + '  motion is ' + str(motionIndex)
					key = key + "_" + motionIndex

					# print "key is motion ========"+ key
					self.preName[dirname] = key
					key = startKey

				if dirname in dirs:
					dirF = '%02d' % int(dirname)
		
					# print 'dir is ' + dirF + " parent is " + parent
					parent = parent.replace('\\','/')
					ks = parent.split('/')
					ks = ks[len(ks) -1]
					key = self.preName[ks] + "_" + dirF

					self.preName[key] = key

					# print 'self.preName is ' + self.preName[key]
	
    def rename(self,filePath,key):
        filelist = os.listdir(filePath)
        total_num = len(filelist)
        i = 1
        preName = self.preName[key]
        for item in filelist:
            if item.endswith('.png'):
                src = os.path.join(os.path.abspath(filePath), item)
                s = "%02d" % i
                dst = os.path.join(os.path.abspath(filePath), preName +'_' +  s + '.png')
                try:
                    os.rename(src, dst)
                    # print 'converting %s to %s ...' % (src, dst)
                    i = i + 1
                except:
                    continue
        # print 'total %d to rename & converted %d jpgs' % (total_num, i)

    def batchRename(self):
		# rootdir = sys.argv[1] 				
		# print("rootdir======" + rootdir)
		# startKey =rootdir.split('\\')[-1:][0] 
		# print("startKey======" + startKey)
    	for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
	    	for dirname in dirnames:
				if dirname in dirs:
					parent = parent.replace('\\','/')
					ks = parent.split('/')
					ks = ks[len(ks) -1]
					motionIndex = motionNames.index(ks) + 1
					motionIndex = '%02d' % motionIndex
					dirPre = dirname
					dirname = '%02d' % int(dirname)
					key = startKey + "_" + motionIndex + "_" + dirname
					self.rename(os.path.join(parent,dirPre),key)

	


if __name__ == '__main__':
    startKey = sys.argv[1]
    rootdir =  rootdir + startKey
    targetDir = targetDir + startKey
    batch=BatchRename()
    batch.batchRename()

    # 拷贝所有资源
    for parent,dirnames,filenames in os.walk(rootdir):
    	for dirname in dirnames:
    		if dirname in dirs:
    			copyFiles(os.path.join(parent,dirname), targetDir)

