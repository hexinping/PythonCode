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


    https://blog.csdn.net/weixin_39909877/article/details/78842536
'''


from xml.dom.minidom import parse
import xml.dom.minidom


def elements_func(root, attrName):

    attrs = root.getElementsByTagName(attrName)
    if not attrs:
        print attrName + "属性不存在"
    else:
        for attr in attrs:
            print attrName+": %s" % attr.childNodes[0].data

def dom_read_fun():

    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse("movies.xml")
    collection = DOMTree.documentElement

    # 查找“shelf”属性
    if collection.hasAttribute("shelf"):
        print "Root element : %s" % collection.getAttribute("shelf")

    # 在集合中获取所有电影
    movies = collection.getElementsByTagName("movie")
    for movie in movies:
        print "*****Movie*****"
        if movie.hasAttribute("title"):
            print "Title: %s" % movie.getAttribute("title")
            # print movie.nodeName, movie.nodeValue


        #获取某个标签下的某个元素 getElementsByTagName

        elements_func(movie, "type")
        elements_func(movie, "format")
        elements_func(movie, "year")
        elements_func(movie, "rating")
        elements_func(movie, "stars")
        elements_func(movie, "description")

#-------------------------------------------------------------------------
#https://www.jb51.net/article/74942.htm

XML_FILE = "movies.xml"
from ElementTree_XML import ElementTree_Class as EleClass

def elementTree_func():

    # 1. 读取xml文件
    eleObj = EleClass(XML_FILE)
    tree = eleObj.read_xml()
    # 2. 属性修改
    # A. 找到父节点
    nodes = eleObj.find_nodes("movie") #拿到所有的movie节点

    for node in nodes:
        # 拿到movie节点的子节点list
        children = node._children
        for child in children:
            print "tag = %s, value = %s" % (child.tag,child.text)

    # B. 通过属性准确定位子节点
    tchilds = nodes[0]._children
    result_nodes = eleObj.get_node_by_keyvalue(tchilds, {"year": "2003"}, True)
    for node in result_nodes:
        print node.tag,node.text

    attrs = result_nodes[0].attrib
    for key, value in attrs.items():
        print "属性1：", key, value

    # C. 修改节点属性 为什么文件内容不变 打出来的值明明变了啊 ==》文件内容不会变 我理解为只拿到了一份数据拷贝
    eleObj.change_node_properties(result_nodes, {"title": "2221"})
    for key, value in attrs.items():
        print "属性2：", key, value

    # D. 删除节点属性
    eleObj.change_node_properties(result_nodes, {"title": ""}, True)

    # 3. 节点修改

    remindNode = nodes[0]
    # A.新建节点
    newTag = "person"
    if not eleObj.check_node_isExist(remindNode,newTag):
        a = eleObj.create_node(newTag, {"age": "15", "money": "200000"}, "this is the firest content")
        # B.插入到父节点之下
        remindNode.append(a)

    if eleObj.check_node_isExist(remindNode, "description"):
        # 4. 删除节点
        # 定位父节点
        # 准确定位子节点并删除之
        eleObj.del_node_by_tagkeyvalue(nodes, "description", {"sequency": "chain1"})


    # 5. 修改节点文本
    # 定位节点
    text_nodes = eleObj.get_node_by_keyvalue(eleObj.find_nodes("movie/description"), {"sequency": "chain1"})
    eleObj.change_node_text(text_nodes, "new text")


    # 6. 输出到结果文件
    eleObj.write_xml(XML_FILE)


if __name__ == "__main__":
    print "xml 解析------"

    # dom_read_fun()

    elementTree_func()