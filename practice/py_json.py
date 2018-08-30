# -*- coding: UTF-8 -*-

'''
    http://www.runoob.com/python/python-json.html

    使用 JSON 函数需要导入 json 库：import json。

    json.dumps	将 Python 对象编码成 JSON 字符串
    json.loads	将已编码的 JSON 字符串解码为 Python 对象


'''

import json

#python原始类型为 JSON 格式数据：
'''
    python 原始类型向 json 类型的转化对照表：

    Python	            JSON
    
    dict	            object
    list, tuple	        array
    str, unicode	    string
    int, long, float	number
    True	            true
    False	            false
    None	            null
'''
def py_to_json():
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

    jsonD = json.dumps(data)
    print jsonD



    #使用参数让 JSON 数据格式化输出：
    print json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': '))

    test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}

    # dump: 将数据写入json文件中
    with open("record.json", "w") as f:
        json.dump(test_dict, f)
        f.close()
        print("加载入文件完成...")

    with open("record.json", 'r') as load_f:
        load_dict = json.load(load_f)
        load_f.close()
        print(load_dict)
    load_dict['smallberg'] = [8200, {1: [['Python', 81], ['shirt', 300]]}]
    print(load_dict)

    with open("record.json", "w") as dump_f:
        json.dump(load_dict, dump_f)
        dump_f.close()


'''
json 类型转换到 python 的类型对照表：
    JSON	        Python
    
    object	        dict
    array	        list
    string	        unicode
    number (int)	int, long
    number (real)	float
    true	        True
    false	        False
    null	        None
'''
def json_to_py():
    #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
    jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

    text = json.loads(jsonData)  #返回一个dict
    print text

    for key,value in text.items():
        print key , value

    jsonData1 = "[2,2,3,4,5]"
    text1 = json.loads(jsonData1)  # 返回一个list
    print text1
    for t in text1:
        print t


#使用第三方库：Demjson  需要下载
'''
    encode	将 Python 对象编码成 JSON 字符串
    decode	将已编码的 JSON 字符串解码为 Python 对象
'''

import  demjson
def demjson_func():
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

    json = demjson.encode(data)
    print json

    data = '{"a":1,"b":2,"c":3,"d":4,"e":5}'  #转换之后是个dict

    text = demjson.decode(data)
    print  text

    for key,value in text.items():
        print key , value

if __name__ == "__main__":
    print "json 解析------"

    py_to_json()

    # json_to_py()

    # demjson_func()