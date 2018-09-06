# -*- coding: UTF-8 -*-


'''
    题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

    程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。

'''

def getLevel(score):
    return (score >= 90) and "A"or ((score >= 60) and "B" or "C")

def isNumInt(x):
    try:
        x=int(x)
        return isinstance(x,int)
    except ValueError:
        return False

def isNumFloat(x):
    try:
        x=float(x)
        return isinstance(x,float)
    except ValueError:
        return False

def func1():

    score = raw_input(">")

    if not score.isdigit():

        if not isNumFloat(score):
            print "请输入数字！！！！！！！！"
            return
        else:
            score = float(score)
            print getLevel(score)

    else:
        score = int(score)
        print getLevel(score)

    # print level



if __name__ == "__main__":
    print "15-----------"
    func1()