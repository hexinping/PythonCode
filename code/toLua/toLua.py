
import xlrd
import io
import os,sys
import time

require_list=[]

reload(sys)
sys.setdefaultencoding('utf-8')
lang='zh_cn'
platform=''
if len(sys.argv)>1:
	lang=sys.argv[1]
if len(sys.argv)>2:
	platform=sys.argv[2]

toolsdir=os.path.split(os.path.realpath(__file__))[0]
os.chdir(toolsdir)

def GenLua(filename,outdir,strid,isLocal=True):
	global require_list
	print "begin handle excel:"+filename

	short_name = filename[:filename.find(".")]+"_conf"
	print "short_name:" + short_name

	wb=xlrd.open_workbook(filename)
	for s in wb.sheets():
		short_name=s.name+"_conf"
		require_list.append((short_name).lower())
		var_name=(short_name).lower()
		filename_gen=(short_name+".lua").lower()
		f=open(outdir + "/"+filename_gen,"wb")

		localname=""
		if(isLocal==True):
			localname="local "
		f.write(localname+var_name+"={\n")

		for row in range(s.nrows):
			if strid:
				if(row>0):
					colkey=s.cell(row,1).value.encode('utf-8')
					coltxt=s.cell(row,2).value.encode('utf-8')
					f.write(colkey.lower()+"= \""+coltxt+"\"")
					if row<s.nrows-1:
						f.write(",\n")
					else:
						f.write("\n")
			else:
				if (row>0):
					item_id=0
					row_str=""
					for col in range(s.ncols):
						if(row>0):
							colname=str(s.cell(0,col).value)
							if colname==None or len(colname)==0 :
								break;
							cellvalue=s.cell(row,col).value

							if cellvalue==None or cellvalue=="":
								continue;


							item_id=s.cell(row,0).value

							if isinstance(cellvalue,basestring):
								if cellvalue.isdigit():
									row_str+="		"+colname+" = "+str(int(cellvalue)) + ""
								else:
									row_str+="		"+colname+" = \""+cellvalue.encode("utf-8") + "\""
							else:
								row_str+="		"+colname+" = "+str(int(cellvalue)) + ""

							if col<s.ncols-1:
								row_str+=",\n"
							else:
								row_str+="\n"

					if isinstance(item_id,basestring):
						row_str="[\'"+str(item_id)+"\']"+"={\n"+row_str
					else:
						row_str="["+str(int(item_id))+"]"+"={\n"+row_str

					f.write(row_str)
					if row<s.nrows-1:
						f.write("},")
					else:
						f.write("}")

					f.write("\n")


		f.write("}\n")

		if isLocal==True:
			f.write("return "+var_name+"\n")

		f.close()

outdirName = "cong_lua"

def traverse(srcpath):
	global i
	for item in os.listdir(srcpath):
		scr_sub_path = os.path.join(srcpath,item)

		if os.path.isdir(scr_sub_path):
			print("dir")
		else:
			if item[0]!='.':
				print("%s" % scr_sub_path[2:])
				if scr_sub_path.find("~$")==-1 and scr_sub_path[-4:]=="xlsx":
					GenLua(scr_sub_path[2:],outdirName,False)

traverse(".")