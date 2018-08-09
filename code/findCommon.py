
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


inputDir  = 'E:/test'                                # 指明被遍历的文件夹
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
		#print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
		outPut.append(os.path.join(parent,filename))
		outPutName.append(filename)

length = len(outPutName)
index = 0

while index<length:
	# print 'filename===========' + outPutName[count]
	filename = outPutName[index]
	num = outPutName.count(filename)
	if num>1:
		# print 'filename===========' + filename + '  num====',num
		# print 'filepath===========' + outPut[index]
		j=0
		pos=0
		while j<num:
			pos=outPutName.index(filename,j+pos)
			if pathList.count(outPut[pos])==0:
				pathList.append(outPut[pos])
			j+=1
		
	index+=1


# f = open('log.txt','w')
# for pathName in pathList:
# 	print 'pathName===========' + pathName
# 	f.write(pathName+'\n')
# f.close()

print 'total count================%d' % len(pathList)

