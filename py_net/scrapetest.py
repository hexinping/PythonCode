# -*- coding: UTF-8 -*-

from urllib.request import urlopen

'''
如果你用过 Python 2.x 里的 urllib2 库，可能会发现 urllib2 与 urllib 有些不同。
在 Python 3.x 里， urllib2 改名为 urllib，被分成一些子模块： urllib.request、
urllib.parse 和 urllib.error。尽管函数名称大多和原来一样，但是在用新
的 urllib 库时需要注意哪些函数被移动到子模块里了
'''

'''
<html>
<head>
<title>A Useful Page</title>
</head>
<body>
<h1>An Interesting Title</h1>
<div>
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</div>
</body>
</html>


'''

from bs4 import BeautifulSoup
from urllib.error import HTTPError

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),features="html.parser")
        title = bsObj.head.title
        h1 = bsObj.body.h1

        '''
            这几种取法是一样的
            bsObj.html.body.h1
            bsObj.body.h1
            bsObj.html.h1
            bsObj.h1
        '''
    except AttributeError as e:
        return None
    return title,h1

if __name__ == "__main__":
    print("1------")

    title, h1 = getTitle("http://www.pythonscraping.com/pages/page1.html")
    if title == None:
        print("Title could not be found")
    else:
        print(title)
        print(h1)