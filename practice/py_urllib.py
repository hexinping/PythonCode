# -*- coding: UTF-8 -*-


import  urllib
import  urllib2


#https://www.jianshu.com/p/cfbdacbeac6e

def url_fun():

    # # 向指定的url地址发送请求，并返回服务器响应的类文件对象
    # response = urllib2.urlopen('http://www.baidu.com/')
    # # 服务器返回的类文件对象支持python文件对象的操作方法
    # # read()方法就是读取文件里的全部内容，返回字符串
    # html = response.read()
    # print html


    ## request: POST
    # http测试：http://httpbin.org/
    data = bytes(urllib.urlencode({'word': 'hello'}))
    args = bytes(urllib.urlencode({'time': 1,'age':12}))
    response = urllib2.urlopen('http://httpbin.org/post?'+args, data=data) #返回一个str
    print(response.read())

    # # 超时设置
    # response = urllib2.urlopen('http://httpbin.org/get', timeout=1)
    # print(response.read())

    response = urllib2.urlopen('http://www.baidu.com')
    print(type(response))
    # 状态码， 响应头

    response1 = urllib2.urlopen('http://www.python.org')

    print response1.code,response1.msg,response1.url
    # print(response1.status)
    print "heads-------"
    # print(response1.headers)

    headers = response1.headers  #字典

    print headers["server"],headers["date"]
    # for key,value in headers.items():
    #     print "key:"+key,"value:"+value



def url_fun2():
    # Request
    # 声明一个request对象，该对象可以包括header等信息，然后用urlopen打开。

    # 简单例子
    # request = urllib2.Request('http://python.org')
    # response = urllib2.urlopen(request)
    # print(response.read().decode('utf-8'))


    # 增加header

    url = 'http://httpbin.org/post'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Host':'httpbin.org'
    }
    # 构造POST表格
    dict = {
        'name': 'Germey',
        'age':  12
    }
    data = bytes(urllib.urlencode(dict))
    req = urllib2.Request(url=url, data=data, headers=headers, origin_req_host ='POST')
    response = urllib2.urlopen(req)
    print(response.read()).decode('utf-8')


import  cookielib
def url_cookie_func():
    # import http.cookiejar

    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    response = opener.open("http://www.baidu.com")
    for item in cookie:
        print(item.name + "=" + item.value)

    # 保存cooki为文本

    filename = "cookie.txt"
    # # 保存类型有很多种
    ## 类型1
    cookie = cookielib.MozillaCookieJar(filename)
    ## 类型2
    cookie = cookielib.LWPCookieJar(filename)

    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    response = opener.open("http://www.baidu.com")

    # 使用相应的方法读取
    # cookie = cookielib.LWPCookieJar()
    # cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    # handler = urllib2.HTTPCookieProcessor(cookie)
    # opener = urllib2.build_opener(handler)
    # response = opener.open("http://www.baidu.com")

def url_parse_func():
    #URL解析
    #主要是一个工具模块，可用于为爬虫提供URL。
    '''

        urlib.parse.urlparse(urlstring,scheme='', allow_fragments=True)
        # scheme: 协议类型
        # 是否忽略’#‘部分

        urlparse模块主要是把url拆分为6部分，并返回元组。并且可以把拆分后的部分再组成一个url。
        主要有函数有urljoin、urlsplit、urlunsplit、urlparse等

        https://blog.csdn.net/qinglu000/article/details/50751900

    '''

    import urlparse as parse
    result = parse.urlparse("https://edu.hellobi.com/course/157/play/lesson/2580")
    #result为一个元组（不可变列表）
    for item in result:
        print item

    #urlunparse:拼接URL，为urlparse的反向操作
    data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
    print(parse.urlunparse(data))

    #urlencode:字典对象转换成GET请求对象
    params = {
        'name': 'germey',
        'age': 22
    }
    base_url = 'http://www.baidu.com?'
    url = base_url + urllib.urlencode(params)
    print(url)



if __name__ == "__main__":
    print "url-------"
    # url_fun2()
    # url_cookie_func()

    # url_error()
    url_parse_func()