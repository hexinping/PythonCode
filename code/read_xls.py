
#_*_ coding:utf-8 _*_

import xlrd

workbook = xlrd.open_workbook('test.xls')

#获取excel中表单数量 workbook.nsheets
nSheet = workbook.nsheets
print '表单数量======='+str(nSheet)

#获取excel中的一个表单
	
sheet1 = workbook.sheets()[0]
sheet2 = workbook.sheet_by_index(1)
sheet3 = workbook.sheet_by_name('python_read')

#.获取行数
print '表单行数==============='+str(sheet1.nrows)
print '表单行数==============='+str(sheet2.nrows)
print '表单行数==============='+str(sheet3.nrows)

print '表单列数==============='+str(sheet1.ncols)
print '表单列数==============='+str(sheet2.ncols)
print '表单列数==============='+str(sheet3.ncols)

#获取整行数据
data_row0 = sheet1.row(0)
for x in data_row0:
	print 'x==============%s' % x

#获取整列数据
data_cl0 = sheet1.col(0)
for x in data_cl0:
	print 'x==============%s' % x

#获取单元格数据
cell_data = sheet1.cell(0, 0).value
print 'cell_data==============%d' % cell_data