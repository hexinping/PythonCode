# -*- coding: UTF-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError


'''
    findAll(tag, attributes, recursive, text, limit, keywords)
    find(tag, attributes, recursive, text, keywords)
    
    你可以传一个标签的名称或多个标签名称组成的 Python
    列表做标签参数。例如，下面的代码将返回一个包含 HTML 文档中所有标题标签的列表： 1
    .findAll({"h1","h2","h3","h4","h5","h6"})
    
    属性参数 attributes 是用一个 Python 字典封装一个标签的若干属性和对应的属性值。例
    如，下面这个函数会返回 HTML 文档里红色与绿色两种颜色的 span 标签：
    .findAll("span", {"class":{"green", "red"}})
    
    递归参数 recursive 是一个布尔变量。你想抓取 HTML 文档标签结构里多少层的信息？如果
    recursive 设置为 True， findAll 就会根据你的要求去查找标签参数的所有子标签，以及子
    标签的子标签。如果 recursive 设置为 False， findAll 就只查找文档的一级标签。
    findAll默认是支持递归查找的（ recursive 默认值是 True）；一般情况下这个参数不需要设置，
    
    文本参数 text 有点不同，它是用标签的文本内容去匹配，而不是用标签的属性。假如我们
    想查找前面网页中包含“ the prince” 内容的标签数量，我们可以把之前的 findAll 方法换
    成下面的代码：
    nameList = bsObj.findAll(text="the prince")
    print(len(nameList))
    输出结果为“ 7”。
    
    范围限制参数 limit，显然只用于 findAll 方法。 find 其实等价于 findAll 的 limit 等于
    1 时的情形。如果你只对网页中获取的前 x 项结果感兴趣，就可以设置它。但是要注意，
    这个参数设置之后，获得的前几项结果是按照网页上的顺序排序的，未必是你想要的那
    前几项。
    
    参数 keyword，可以让你选择那些具有指定属性的标签。例如：
    allText = bsObj.findAll(id="text")
    print(allText[0].get_text())
    
    bsObj.findAll(id="text")
    bsObj.findAll("", {"id":"text"})

'''

import Utils


if __name__ == "__main__":
    print('2-------')

    url = "http://www.pythonscraping.com/pages/warandpeace.html"
    # url = "https://mail.126.com/"
    bsObj = Utils.getBsObj(url)


    # nameList = bsObj.findAll("a", {"target": "_blank"})

    nameList = bsObj.findAll("span", {"class": "green"})

    for name in nameList:
        print(name.get_text())