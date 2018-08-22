# -*- coding: UTF-8 -*-


'''
https://www.cnblogs.com/shaosks/p/7344771.html
YAML 语言（发音 /ˈjæməl/ ）的设计目标，就是方便人类读写。它实质上是一种通用的数据串行化格式。

　　　　它的基本语法规则如下：

　　　　1、大小写敏感

　　　　2、使用缩进表示层级关系

　　　　3、缩进时不允许使用Tab键，只允许使用空格。

　　　　4、缩进的空格数目不重要，只要相同层级的元素左侧对齐即可

　　　　5、# 表示注释，从这个字符一直到行尾，都会被解析器忽略，这个和python的注释一样



　　　　YAML 支持的数据结构有三种：

　　　　1、对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）

　　　　2、数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）

　　　　3、纯量（scalars）：单个的、不可再分的值。字符串、布尔值、整数、浮点数、Null、时间、日期

'''

import  os
import  yaml

def yaml_func():

    try:


        f = open("config.yaml","rb")
        cont = f.read()

        #加载yaml内容
        cf = yaml.load(cont)

        #获取某个字段
        db = cf.get('db')

        for key, value in db.items():
            print key, value

        str1 = cf.get("str1")
        str3 = cf.get("str3")
        strline = cf.get("strline")

        print str1,str3
        print "strline:",strline

        this = cf.get("this")   #换行
        print "this:",this

        that = cf.get("that")   #不换行
        print "that:", that

        animal = cf.get("animal")
        print "animal:",animal

        dict1 = cf.get("dict1")
        print "dict1:", dict1

        animal2 = cf.get("animal2")
        print "animal2:", animal2

    except IOError:
        print "文件不存在-------"


if __name__ == "__main__":

    print "yaml--------"
    yaml_func()