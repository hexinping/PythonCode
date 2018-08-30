# -*- coding: UTF-8 -*-

#https://www.cnblogs.com/yanglang/p/7126660.html

import  csv


CSV_FILE = "hero.csv"
CSV_FILE1 = "test.csv"


def utf_to_gb2312(data):
    return data.decode('GB2312').encode('utf-8')

def csv_read():

    with open(CSV_FILE) as f:

        reader = csv.reader(f)
        # reader = reader.decode("utf-8")
        datas = list(reader)



        # data不能直接打印，list(data)
        # 最外层是list，里层的每一行数据都在一个list中，有点像这样
        # print(list(reader))

        #下标从0开始
        # print datas[0][0]
        #
        # for row in reader:
        #     # 行号从1开始
        #     print(reader.line_num, row)

        #遍历数据
        csvDatas = []

        # for row in datas:
        #     for col in row:
        #         print col


        rowCount = len(datas)
        keys = datas[0]
        colCount = len(keys)

        print rowCount,colCount
        for row in range(rowCount):
            t = []
            for col in range(colCount):
                str = utf_to_gb2312(datas[row][col])
                str.replace(' ','')  #去掉空格
                str.replace('\n', '').replace('\n', '') #去掉换行
                print "row:%s,col:%s, %s" % (row, col, str)

                t.append(datas[row][col])

            csvDatas.append(t)




def csv_write():
    # 使用数字和字符串的数字都可以


    datas = [[1002,"CHINESE_1","profession1"],[1003,"CHINESE_3","profession3"]]

    with open(CSV_FILE, 'ab') as f:
        writer = csv.writer(f)

        #单行写入
        # for row in datas:
        #     writer.writerow(row)

        # 还可以写入多行
        writer.writerows(datas)

def csv_dic_rw():
    '''
    DictReader和DictWriter对象
    使用DictReader可以像操作字典那样获取数据，把表的第一行（一般是标头）作为key。可访问每一行中那个某个key对应的数据。

    '''
    with open(CSV_FILE) as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Max TemperatureF是表第一行的某个数据，作为key
            max_temp = row["id$c"]
            max_temp = utf_to_gb2312(max_temp)
            print(max_temp)


    #使用DictWriter类，可以写入字典形式的数据，同样键也是标头（表格第一行）。
    headers = ['name', 'age']

    datas = [{'name': 'Bob', 'age': 23},
             {'name': 'Jerry', 'age': 44},
             {'name': 'Tom', 'age': 15}
             ]

    with open(CSV_FILE1, 'wb') as f:
        # 标头在这里传入，作为第一行数据
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        # for row in datas:
        #     writer.writerow(row)

        # 还可以写入多行
        writer.writerows(datas)


if __name__ == "__main__":
    print "csv---------------"

    # csv_read()
    # csv_write()
    csv_dic_rw()