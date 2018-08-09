
#_*_ coding:utf-8 _*_

# 使用方法
# 当图片全在一个文件夹内(没有子文件夹) python Tp.py E:/test 0
# 当文件夹有子文件夹时  python Tp.py E:/test/  1

import sys
import os
import os.path
import shutil 

inputDir 	= sys.argv[1]  							    #导入路径
is_outPut 	= sys.argv[2]								#遍历输出==1 或者 直接输出==0
outPlist 	= []


def TpCommand(prarentdir, dirname):

	pngStr = ''
	if prarentdir.endswith('/'):
		pngStr = prarentdir
	else:
		pngStr = prarentdir + '/'

	commandStr 		= []

	# 导出到与图片相同路径
	outPutPng  		= pngStr + dirname + '/' + dirname + '.png'
	outPutPlist  	= pngStr + dirname + '/' + dirname + '.plist'

	commandStr.append('TexturePacker') 						#Tp 命令
	commandStr.append(pngStr + dirname) 					#输入文件目录
	commandStr.append('--sheet ' +  outPutPng ) 			#导出png名称
	commandStr.append('--data '  + outPutPlist )			#导出plist名称
	commandStr.append('--allow-free-size')					#允许非2的幂次方
	commandStr.append('--trim')								#裁剪图片周围透明像素
	commandStr.append('--max-size 4096')					#导出最大尺寸
	commandStr.append('--format cocos2d')					#导出符合格式
	

	#导出plist路径
	# path 			= pngStr+dirname+'/'+dirname
	# plistpath		= path + '.plist'
	# plistpath 	= plistpath.replace('E:/test', 'plist')
	# outPlist.append(plistpath)


	os.system(' '.join(commandStr))



def Traversal():

	for parent,dirnames,filenames in os.walk(inputDir):     #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

		for dirname in dirnames:							 #输出文件夹信息

			# print 'parent is:' + parent
			# print 'dirname is :' + dirname
			TpCommand(parent, dirname)
			

#  -opt RGBA4444
def outPut():
	path   = inputDir.split('/')
	length = len(path)
	outPutPng  		= inputDir + '/' + path[length-1] + '.png'
	outPutPlist  	= inputDir + '/'+ path[length-1] + '.plist'
	command   		= 'TexturePacker '+inputDir+' --sheet '+outPutPng+' --data '+outPutPlist\
			 		  +' --allow-free-size --trim --max-size 4096 --format cocos2d'
	os.system(command)



#把某一目录下的所有文件复制到指定目录中 目标文件不存在新建一个
def copyFiles(sourceDir,  targetDir): 

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


# 写入文件 
def writeToFile(file,sourceDir,tarGetDir):

	f = open(file,'w')
	for pathName in outPlist:
		f.write(pathName+'\n')
	f.close()

	if tarGetDir and sourceDir:
		copyFiles(sourceDir,tarGetDir)


if __name__ == '__main__':

	if is_outPut=='0':
	  outPut()
	else:
 	  Traversal()
 	  #writeToFile('TexturePlistConfig.txt')







