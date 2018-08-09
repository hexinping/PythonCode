#_*_ coding:utf-8 _*_

import xlrd
fileOutput = open('test.lua','w')
workbook = xlrd.open_workbook('test.xls')
sheet = workbook.sheet_by_name('keyData')

# for row in xrange(sheet.nrows):
# 	for col in xrange(sheet.ncols):
# 		cell_data = sheet.cell(row,col).value
# 		print 'cell_data==============%s  %s' % cell_data

# 可以在这里写一些固定的注释代码之类的
writeData = "-- @author:hexinping\n\n\n"

writeData = writeData + sheet.name + ' = {\n'
# for col in xrange(sheet.ncols):
# 	for row in xrange(sheet.nrows):
# 		value = sheet.cell(row, col).value
# 		if  row == 0 :
# 			writeData = writeData + '\t' + '["' + value + '"]' + ' = ' + '{ '  
# 		else :
# 			writeData = writeData + '"' + str(sheet.cell(row, col).value) + '" , '
# 	else :
# 		writeData = writeData + '} ,\n'
# else :
# 	writeData = writeData + '}\n\n'


keyName = []
for row in xrange(sheet.nrows):
	for col in xrange(sheet.ncols):
		value = sheet.cell(row, col).value
		if  row == 0 :			
			keyName.append(str(value)) 
		else :			
			if col == 0:
				writeData = writeData + '\t'+ keyName[col]+str(int(value)) + ' = ' +'\t'+ '{ '		
			else:
				if isinstance(value, (float,int)):
					writeData = writeData + keyName[col] + '=' + '"' + str(int(value)) + '" , '					
				else:
					writeData = writeData + keyName[col] + '=' + '"' + str(value) + '" , '				
	else :
		if row!=0:
			writeData = writeData + '} ,\n'
else :
	writeData = writeData + '}\n\n'


fileOutput.write(writeData)

fileOutput.close()