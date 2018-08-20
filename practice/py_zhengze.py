
# -*- coding: UTF-8 -*-

'''
    python 正则表达式 操作

    re 模块使 Python 语言拥有全部的正则表达式功能。

    http://www.runoob.com/python/python-reg-expressions.html


    [Pp]ython	匹配 "Python" 或 "python"
    rub[ye]	    匹配 "ruby" 或 "rube"
    [aeiou]	    匹配中括号内的任意一个字母
    [0-9]	    匹配任何数字。类似于 [0123456789]
    [a-z]	    匹配任何小写字母
    [A-Z]	    匹配任何大写字母
    [a-zA-Z0-9]	匹配任何字母及数字
    [^aeiou]	除了aeiou字母以外的所有字符
    [^0-9]	    匹配除了数字外的字符

    .	匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
    \d	匹配一个数字字符。等价于 [0-9]。
    \D	匹配一个非数字字符。等价于 [^0-9]。
    \s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
    \S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
    \w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
    \W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。


    re*	匹配0个或多个的表达式。
    re+	匹配1个或多个的表达式。
    re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
    ^	匹配字符串的开头
    $	匹配字符串的末尾。
    re{ n}	    精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
    re{ n,}	    匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
    re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
    a| b	    匹配a或b
    (re)	    匹配括号内的表达式，也表示一个组

'''


import re





def re_func():

    #re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回None。
    #re.match(pattern, string, flags=0)
    print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
    print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配


    #re.search 扫描整个字符串并返回第一个成功的匹配。
    print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
    print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

    '''
        re.match与re.search的区别
            re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
            re.search匹配整个字符串，直到找到一个匹配。
    '''

    line = "Cats are smarter than dogs"
    matchObj = re.search(r'(.*) are (.*?) .*',line,re.M|re.I)
    if matchObj:
        print "matchObj.group() : ", matchObj.group()
        print "matchObj.group(1) : ", matchObj.group(1)
        print "matchObj.group(2) : ", matchObj.group(2)
    else:
        print "No match!!"



    #re 模块提供了re.sub用于替换字符串中的匹配项。

    phone = "2004-959-559 # 这是一个国外电话号码"

    # 删除字符串中的 Python注释
    num = re.sub(r'#.*$', "", phone)
    print "电话号码是: ", num

    # 删除非数字(-)的字符串
    num = re.sub(r'\D', "", phone)
    print "电话号码是 : ", num

    # 将匹配的数字乘以 2
    def double(matched):
        value = int(matched.group('value'))
        return str(value * 2)

    s = 'A23G4HFD567'
    print(re.sub('(?P<value>\d+)', double, s))


    #findall 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
    '''
        findall(string[, pos[, endpos]])
            参数：
            
            string : 待匹配的字符串。
            pos : 可选参数，指定字符串的起始位置，默认为 0。
            endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。

    '''

    patten = re.compile(r'\d+')  # 查找数字
    result1 = patten.findall("ddddd444eeee666e22")
    print result1

    result2 = patten.findall('run88oob123google456', 0, 10)
    print result2

    #字典形式取出
    s = '1102231990xxxxxxxx'
    res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{3})', s)
    print(res.groupdict())
    #此分组取出结果为：
    #{'province': '110', 'city': '223', 'born_year': '199'}


if __name__ == "__main__":
    print "正则表达式------------"

    re_func()