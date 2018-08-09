
#_*_ coding:utf-8 _*_
#########################################
# import sys
# import os
# #command = 'mspaint'
# inputDir = sys.argv[1]
# # command  = 'TexturePacker E:/test --sheet E:/test/out.png --data E:/test/out.plist \
# # 			--allow-free-size --no-trim --max-size 1024 --format cocos2d '
# command   =  'TexturePacker '+inputDir+' --sheet '+inputDir+'/out.png'+' --data '+inputDir+'/out.plist'\
# 			 +' --allow-free-size --no-trim --max-size 1024 --format cocos2d'
# os.system(command)
#########################################
# 使用方法
# 当图片全在一个文件夹内(没有子文件夹) python Tp.py E:/test E:/plist 0
# 当文件夹有子文件夹时  python Tp.py E:/test/ E:/plist 1
# 调用 python Tp.py E:/test E:/plist
# 
import sys
import os
import os.path
#inputDir 	= sys.argv[1]
#plistDir 	= sys.argv[2]
#is_outPut 	= sys.argv[3]


inputDir  = 'E:/test/plist'                                # 指明被遍历的文件夹
#plistDir =  'E:/plist/'

outPut = []
outPutName = []

pathList = []

for parent,dirnames,filenames in os.walk(inputDir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

	# for dirname in dirnames:						#输出文件夹信息
	# 	print 'parent is:' + parent
	# 	print 'dirname is :' + dirname

	for filename in filenames:    				#输出文件信息
		#print 'parent=%s'  % parent
		#print 'filename=%s' % filename
		# print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息

		if filename.endswith('.plist'):

			plistPath = os.path.join(parent,filename)
			plistPath = plistPath.replace('\\', '/')
			plistPath = plistPath.replace('E:/test/', '')
			outPut.append(plistPath)
		# outPutName.append(filename)

# 写入文件 
def writeToFile(file):

	f = open(file,'w')
	for pathName in outPut:
		f.write(pathName+'\n')
	f.close()

writeToFile('TexturePlistConfig.txt')