# -*- coding: UTF-8 -*-

'''
    xml 解析

    http://www.runoob.com/python/python-xml.html

    python有三种方法解析XML，SAX，DOM，以及ElementTree

     1.SAX (simple API for XML )
        python 标准库包含SAX解析器，SAX用事件驱动模型，通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件。

     2.DOM(Document Object Model)
        将XML数据在内存中解析成一个树，通过对树的操作来操作XML

     3.ElementTree(元素树)
        ElementTree就像一个轻量级的DOM，具有方便友好的API。代码可用性好，速度快，消耗内存少。


    注：因DOM需要将XML数据映射到内存中的树，一是比较慢，二是比较耗内存，而SAX流式读取XML文件，比较快，占用内存少，但需要用户实现回调函数（handler）。

'''


if __name__ == "__main__":
    print "xml 解析------"