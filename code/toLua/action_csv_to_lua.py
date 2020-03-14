# coding:utf-8
"""csv转lua

Usage:
    action_csv_to_lua.py --input-path=<path> [options]
    action_csv_to_lua.py (-h | --help)

Options:
  -h --help             Show this screen.
  --input-path=<path>   输入路径
  --output-path=<path>  lua输出路径
  --joutput-path=<path>  json输出路径
  

"""

import csv
import json
import os
import copy
import sys

import shutil
import subprocess
import re
zhPattern = re.compile(u'[\u4e00-\u9fa5]+')

# 语言表数组
LANG_ARRAY = []

def isNumber(num):
	try:
		('float', 'int')[round(float(num)) == float(num)]
		return True
	except:
		return False

def isSpecial(str):
	try:
		if is_chinese(str):
			return False
		if str.isdigit() or str.isalpha() or str.isalnum():
			return False
		return True
	except:
		return True
def run(config):
	project_root = config['project_root']
	csvDir = os.path.join(project_root, config['configCsv_input_path1'])

	output_project_root = config['output_project_root']

	luaDir = os.path.join(output_project_root, config['config_output_path1'])
	runList(csvDir, luaDir)

	#复制新手引导文件
	target_dir = ""
	src_path = os.path.join(project_root, config['configCsv_input_path'].replace("csv", "guide"))
	if sys.platform == 'darwin':
		target_dir = luaDir
		args = ["rsync", "-Cavz"]
		args.append(src_path)
		args.append(target_dir)
		subprocess.call(args)
	elif sys.platform == 'win32':
		target_dir = os.path.join(luaDir, "guide")
		for dirpath, dirnames, filenames in os.walk(src_path):
			for filename in filenames:
				fullname = os.path.join(dirpath, filename)
				relpath = os.path.relpath(fullname, src_path)  # 得到相对目录，fullname相对于src_path的目录
				dest_filename = os.path.join(target_dir, relpath)
				dest_dirname = os.path.dirname(dest_filename)  #返回文件所在文件夹
				if os.path.exists(dest_dirname) == False:
					os.makedirs(dest_dirname)
				shutil.copy(fullname, dest_filename)
	print("copy guide done")

	#复制AnimAp文件
	target_dir = ""
	src_path = os.path.join(project_root, config['configCsv_input_path'].replace("csv", "battle"))
	if sys.platform == 'darwin':
		target_dir = luaDir
		args = ["rsync", "-Cavz"]
		args.append(src_path)
		args.append(target_dir)
		subprocess.call(args)
	elif sys.platform == 'win32':
		target_dir = os.path.join(luaDir, "battle")
		for dirpath, dirnames, filenames in os.walk(src_path):
			for filename in filenames:
				fullname = os.path.join(dirpath, filename)
				relpath = os.path.relpath(fullname, src_path)
				dest_filename = os.path.join(target_dir, relpath)
				dest_dirname = os.path.dirname(dest_filename)
				if os.path.exists(dest_dirname) == False:
					os.makedirs(dest_dirname)
				shutil.copy(fullname, dest_filename)
	print("copy AnimAP done")
# 拆分lang表
def splitLang(luaDir, lang, langvalue):
	print("splitLang", lang, langvalue)

	valueMap = {}
	valueArr = []

	keyMap = {}
	keyArr = []


	newStrs1 = [] #旧文件
	newStrs2 = [] #新文件

	#LANG_ARRAY 是语言表以及其他配置表里需要语言配置的  存的是列表 [属性，属性值]
	for i in range(0, len(LANG_ARRAY)):
		# key
		key = LANG_ARRAY[i][0].encode('utf-8')
		keyArr.append(key)
		# value
		value = LANG_ARRAY[i][1].encode('utf-8')
		if valueMap.has_key(value):
			pass
		else:
			valueMap[value] = len(valueArr) + 1
			valueArr.append(value)
		index = valueMap[value]
		keyMap[key] = index

	# 输出成lua文件，起始就是把字符串都追加到列表中，然后一起输出
	newStrs1.append("local data_lang")
	newStrs1.append(" = {\n")
	for index, key in enumerate(keyArr):
		newStrs1.append("[\"" + key.decode('utf-8') + "\"]="+str(keyMap[key])+",  --[==[ " + valueArr[keyMap[key] -1].decode('utf-8') + " ]==]\n")
	newStrs1.append("} return data_lang" + "\n")
	__str = ''.join(newStrs1)

	#写入lua文件  lang.lua
	with open(luaDir + '/'+lang+'.lua', 'w', 2) as luaFile:
		#数组字符串替换
		luaFile.write(__str.encode('utf-8'))


	newStrs2.append("local data_langvalue")
	newStrs2.append(" = {\n")
	for index, value in enumerate(valueArr):
		strValue = ""
		if value.decode('utf-8').find('\\n') == 0:
			strValue = '\\n' + value
		else:
			strValue = value
		newStrs2.append("--[[Index:" + str(index + 1) + "]] " + " [=[" + strValue.decode('utf-8').replace('\\n','\n') + "]=],\n")
	newStrs2.append("} return data_langvalue" + "\n")
	__str = ''.join(newStrs2)
	# 写入lua文件  langvalue.lua
	with open(luaDir + '/'+langvalue+'.lua', 'w', 2) as luaFile:
		#数组字符串替换
		luaFile.write(__str.encode('utf-8'))

	sys.stdout.write("\r" + "#### split: ["+lang+"] => ["+lang+"] + ["+langvalue+"]                            ")
	sys.stdout.flush()

def is_chinese(contents):
	match = zhPattern.search(contents)
	if match:
		return True
	else:
		return False

#输出屏蔽字表
def runOutBlockWorlds(contents,luaPath):
	result = {}
	flagPosition = {}
	for key in contents:
		des = key.replace(' ','')
		if False:
			if not result.has_key(key):
				result[key] = 1
		else:
			tempDic = result
			i = 0
			for singleWord in des.decode('utf-8'):
				i = i + 1
				if isSpecial(singleWord):
					continue
				if not tempDic.has_key(singleWord):
					if i == len(des.decode('utf-8')):
						tempDic[singleWord] = {'flag':'true'}
					else:
						tempDic[singleWord] = {}
				else:
					if i == len(des.decode('utf-8')):
						if not tempDic[singleWord].has_key('flag'):
							tempDic[singleWord]['flag'] = 'true'
					pass
				tempDic = tempDic[singleWord]
	strs = []
	strs.append("local data_")
	strs.append('words')
	strs.append(" = {")
	line = 0
	isSecond =False
	for key in result.keys():
		strs.append('["' + key + '"]=1,')
	strs.append("}\n")
	totalLine = len(result.items())
	for key,value in result.items():
		line = line + 1
		if line == 1:
			strs.append('local function WORD' + str(line) + '()\n')
		elif line > totalLine*0.5 and isSecond == False:
			isSecond = True
			strs.append('    end\n')
			strs.append('local function WORD' + str(2) + '()\n')
		strs.append('    data_words')
		strs.append('["')
		strs.append(key)
		strs.append('"]={')
		strs.append(getStrDes(value))
		if getStrDes(value) == '':
			strs.append('flag=true')
		strs.append('}\n')
		if line == totalLine:
			strs.append('    end\n')
			strs.append('    WORD1()\n')
			strs.append('    WORD2()\n')
	strs.append("return data_" + 'words' + "\n")
	strData = ''.join(strs)
	with open(luaPath, 'w', 2) as luaFile:
		#数组字符串替换
		luaFile.write(strData.encode('utf-8'))
def getStrDes(dic):
	i = 0
	subStr = ''
	isDethest = True
	for key,value in dic.items():
		if key == 'flag':
			continue
		i = i + 1
		if i != 1:
			subStr = subStr + ','
		subStr = subStr + '["'
		subStr = subStr + key
		subStr = subStr + '"]'
		subStr = subStr + '='
		if len(value) == 0:
			subStr = subStr + 'true'
		else:
			subStr = subStr + '{'
			isHave = False
			try:
				if value.has_key('flag'):
					isHave = True
			except:
				pass
			if isHave:
				subStr = subStr + 'flag=true,'
			subStr = subStr + getStrDes(value)
			subStr = subStr + '}'
		if len(value) > 0:
			isDethest = False
	return subStr

def runList(csvDir, luaDir):
	reload(sys)  #用于重新载入之前载入的模块。 重新载入sys
	sys.setdefaultencoding('gbk')
	LANG_ARRAY = []
	luaFiles = []
	for dirpath, disnames, filenames in os.walk(csvDir):
			for name in filenames:
				if '.git' not in dirpath and '.git' not in name and '.svn' not in dirpath and '.svn' not in name and '.DS_Store' not in dirpath and '.DS_Store' not in name:
					filepath, filename = os.path.split(csvDir + '/' + name)  #把路径分割成dirname和basename，返回一个元组
					ext = os.path.splitext(filename)  #分割路径，返回路径名和文件扩展名的元组
					filename = filename[0:filename.find('.')]
					sys.stdout.write("\r" + "#### operate: ["+ filename + "]                            ")
					sys.stdout.flush()

					tablename = filename

					if luaDir != None and luaDir != "":
						lua = convertCsvToLua(csvDir + '/' + filename + '.csv', luaDir + '/' + tablename + '.lua')
						if lua:
							luaFiles.append(filename)

	if luaDir != None and luaDir != "":
		splitLang(luaDir, "lang", "langvalue")



	# removeDir(config['project_root'] + "/svn/Resources/script/game/config/guide")
 #    os.mkdir(config['project_root'] + "/svn/Resources/script/game/config/guide")
 #    copyFiles(config['project_root'] + "/svn/configCsv/guide", config['project_root'] + "/svn/Resources/script/game/config/guide")					

	print("\nlua convert Success!!, count: " + str(len(luaFiles)))


def openCsv(csvPath):
	csvFile = open(csvPath, mode='r')

	data = csvFile.read()
	try:
		data.decode(encoding="gbk")
	except UnicodeDecodeError:
		try:
			data.decode(encoding="utf-8")
			print("utf-8")
			return [], ""	
		except UnicodeDecodeError:
			print("unkonwn")
			return [], ""

	csvFile.seek(0)
	firstLine = csvFile.readline()  #读取一行   （第一行为字段属性）
	csvFile.readline()              #读取下一行
	secondLine = csvFile.readline() #读取下一行 （这一行主要是字段定义使用类型（客户端用还是服务器用））
	firstLine = firstLine[0:len(firstLine) - 1].replace('\r', '')
	secondLine = secondLine[0:len(secondLine) - 1].replace('\r', '')
	# 第一列的字头为key
	key = firstLine[0:firstLine.find(',')]

	
	KeyArr = firstLine.split(",")    # 每一列的主键
	AttrArr = secondLine.split(",")  # 每一列的主键对应的属性
	key_attr = {}
	# print(csvPath)
	for i in range(0, len(KeyArr)):
		if i < len(AttrArr) and KeyArr[i] != '':
			key_attr[KeyArr[i]] = AttrArr[i]
	key_attr[key] = 'both'

	csvFile.seek(0)
	csvDict = list(csv.DictReader(csvFile, restkey=None, restval=None))  ####### 得到csv中的所有行，每一行是个字典，以第一行为key值
	if len(csvDict) <= 0 :
		print("null")
		return [], key, key_attr
	csvFile.close()
	#删除前5行
	for i in range(1, 5):
		if len(csvDict) > 0:
			del csvDict[0]
	return csvDict, key, key_attr
			

def convertCsvToLua(csvPath, luaPath):
	csvDict, key, key_attr = openCsv(csvPath)
		
	count = len(csvDict)
	if count <= 0:
		return
	hasLanguage = False
	clientKeys = []
	deleteKey = {}

	filepath, filename = os.path.split(luaPath)
	ext = os.path.splitext(filename)
	filename = filename[0:filename.find('.')]

	#csvDict 是csv表中第6行开始的列表，列表中每一个元素是字典
	cell = csvDict[0]

	#其实就是过滤下第一行第一列的非法情况
	while 1:
		if cell[key] != '' and cell[key][0:1] != '#':
			break
		del csvDict[0]
		cell = csvDict[0]

	count = len(csvDict)
	lang_map = {}
	attr = ''

	if filename == 'l':     #语言表
		# 纯种语言表
		for k in cell.keys(): # k的值为第6行的属性(cn, languageid)
			if k != '':
				if key_attr[k] == 'language':
					if k == 'cn':
						for i in range(0, count):
							if csvDict[i][key] != '' and csvDict[i][key].find('#') == -1:
								LANG_ARRAY.append([csvDict[i][key], csvDict[i][k].replace('#','')]) #设置[属性,属性值]
					else:
						# 多语言
						for i in range(0, count):
							if csvDict[i][key] != '' and csvDict[i][key].find('#') == -1:
								LANG_ARRAY.append([csvDict[i][key] + '_' + k.upper(), csvDict[i][k].replace('#','')])		
		return
	elif filename == 'words':  #屏蔽字
		worlds = []
		for k in cell.keys():
			if k != '':
				if k == 'block':
					for i in range(0, count):
						worlds.append(csvDict[i][k].encode('utf-8'))	
		runOutBlockWorlds(worlds,luaPath)	
		return
	else:
		#其他配置表
		for k in cell.keys():
			if k != '':
				attr = key_attr[k]
				if attr == 'client' or attr == 'both':
					clientKeys.append(k)
				elif attr == 'language':
					# 语言表
					for i in range(0, count):
						if csvDict[i][key] != '' and csvDict[i][k] != '':
							_key = (filename + '_' + k + '_' + csvDict[i][key]).upper()
							_value = csvDict[i][k].replace('#','')
							LANG_ARRAY.append([_key, _value])
							lang_map[_key] = _value
							csvDict[i][k] = _key
							hasLanguage = True
				else:
					deleteKey[k] = True
	#如果只有第一列主键key说明改表无需输出
	if(len(clientKeys) == 1 and hasLanguage == False):
		return
	#转lua
	#深拷贝
	luaDict = copy.deepcopy(csvDict)
	exists = os.path.exists(luaPath)

	strs = []
	if not exists:
		strs.append("local data_")
		strs.append(filename)
		strs.append(" = {\n")
	
	for i in range(0, count):
		#改变key
		for k, v in deleteKey.items():
			del luaDict[i][k]
				
		#删除空值
		luaDict[i] = dict(filter(lambda x: x[1] != "", luaDict[i].items()))
	firstKeyCache = {}	
	luaSuccess = False
	if luaDict[0] != {}:#没有列需要导出, 所以不生成文件
		out = [obj for obj in luaDict]  #遍历luaDict 然后把里面的元素放入out中，out是个list
		
		index = 0
		for i in range(0, count):
			luaList = []
			id = None
			has = False
			for k, v in luaDict[i].items():
				has = True
				if v == None :
					continue
				luaList.append([k, v])  #把属性和属性值记录下
				if k == key: #第一列的主键
					id = v
			luaList.sort()
			if has:
				#过滤注释
				if id == None:
					continue
				if id.find('#') != -1:
					continue
				index = index + 1
				if isNumber(id):
					strs.append("    [")
					strs.append('%d' %int(id))
					strs.append("]={")
				else:
					strs.append('    ["')
					strs.append(id)
					strs.append('"]={')		
			idx = 1

			#检测是否存在重复key值
			if  firstKeyCache.has_key(str(id)):
				raise RuntimeError("filename '" + filename + "' has key '" + str(id) +"'")
			if id != None:
				firstKeyCache[str(id)] = 1

			#输出每一行的lua表结构
			for item in luaList:
				if item[0] == '':
					continue
				if item[0] == key:
					if not isNumber(id):
						continue
					if idx != 1:
						strs.append(",")
					strs.append('id')
				else:
					if idx != 1:
						strs.append(",")
					strs.append(item[0])  #设置属性
				strs.append("=")
				if item[1] == '#REF!':
					print('\n#REF! ' + filename + " error, id=" + id + " key=" + item[0])
				if item[1] == '#N/A':
					print('\n#N/A ' + filename + " error, id=" + id + " key=" + item[0])
				if item[1].count('\n') > 0:
					print('\n\\n ' + filename + " error, id=" + id + " key=" + item[0])
				if item[1].count('#') > 0:
					strs.append('"')
					strs.append(item[1].replace('#',''))  #设置属性值
					strs.append('"')		
				else:

					if item[1].encode('utf-8').count('[') > 0:
						if item[1].encode('utf-8').count('[') != item[1].encode('utf-8').count(']'):
							print('\n[ ]' + filename, "error id-" + id + " key=" + item[0])
						# 设置属性值 属性值为表结构
						strs.append(item[1].encode('utf-8').replace('[','{').replace(']','}').replace('，',',').decode('utf-8'))
					else:
						if isNumber(item[1]):  #整数
							strs.append(item[1])
						else:
							#字符串
							strs.append('"')
							strs.append(item[1])
							strs.append('"')

							#语言表解释追加
							if lang_map.has_key(item[1]):
								strs.append('--[=[')
								value = lang_map[item[1]].decode('gbk')
								if len(value) > 8:
									value = value[0:4].encode('gbk') + '...' + value[len(value) - 4:len(value)].encode('gbk')
								else:
									value = value[0:8].encode('gbk')
								strs.append(value)
								strs.append(']=]')
							
						
				idx = idx + 1
				
			if len(luaList) > 0:		
				strs.append("},\n")


		#整个表的lua结构结尾
		if not exists:
			strs.append("} return data_" + filename + "\n")
			# strs.append("} function data_" + filename + ".dtor() data_" + filename + " = nil end return data_" + filename + "\n")

		if not exists:
			strData = ''.join(strs)  # 拼接成字符串
			with open(luaPath, 'w', 2) as luaFile:
				#数组字符串替换
				sys.stdout.write("\r" + "#### proc: ["+ filename + "]                            ")
				sys.stdout.flush()
				luaFile.write(strData.encode('utf-8')) #写入文件
		else:
			fp = file(luaPath)
			lines = []
			for line in fp: # 内置的迭代器, 效率很高
			    lines.append(line.decode('utf-8'))
			fp.close()

			strData = ''.join(strs)
			lines.insert(len(lines) - 2, strData) 
			s = ''.join(lines)
			with open(luaPath, 'w', 2) as luaFile:
				#数组字符串替换
				sys.stdout.write("\r" + "#### proc: ["+ filename + "]                             ")
				sys.stdout.flush()
				luaFile.write(s.encode('utf-8'))
		luaSuccess = True

	return luaSuccess

if __name__ == '__main__':
  	from docopt import docopt
   	arguments = docopt(__doc__, version='Naval Fate 2.0')
   	# input_path = arguments['--input-path']
   	# output_path = arguments['--output-path']
   	# json_output_path = arguments['--joutput-path']
   	input_path = "D:/GitResponse/PythonCode/code/toLua"
   	output_path = input_path + "/config_lua"
  	runList(input_path,json_output_path,output_path)

#    
#run()
