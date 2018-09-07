# -*- coding: UTF-8 -*-

'''
    题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

    程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。

'''


def func1():

    input_str = raw_input(">")

    # 最简单的方法
    # count = len(input_str)
    # print  count

    # 方法2 去掉换行符
    input_str.replace('\r', '').replace('\n', '').replace('\t', '')
    count = len(input_str)
    print count


def func2():
    '''
        x为一个字符串

        x.isalnum() #判断是否是数字或者是字母

        x.isalpha() #判断字符串第一个是否是字母

        x.isdigit() #判断字符是否是数字组成

        x.islower() #判断字符中是否是小写字母（字符串中可以包含数字，返回为true）

        x.isupper() #判断字符中是否是大写字母（字符串中可以包含数字，返回为true）

        x.isspace() #判断字符是否为空格，其中换行符（\n）、回车符（\r）、换页符（\f）均返回true

        x.istitle() #判断第一个字母是否为大写字母


        '''


    import string
    s = raw_input('请输入一个字符串:\n')
    letters = 0
    space = 0
    digit = 0
    others = 0
    for c in s:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        else:
            others += 1
    print 'char = %d,space = %d,digit = %d,others = %d' % (letters, space, digit, others)

if __name__ == "__main__":
    print '17----------'
    # func1()
    func2()
