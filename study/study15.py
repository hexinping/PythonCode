# #_*_ coding:utf-8 _*_


import  Utils
import study14


from UtilsClass import MathUtils


def module_func():
    print "dddd"

    '''
        使用类而非模块的原因如下：
            类，重复创建出很多出来，哪怕是一次一百万个，它们也不会互相干涉到。
            对于模块来说，当你一次 import 之后，整个程序里就只有这么一份内容，不同文件使用同一个变量会有影响

    '''
    print Utils.add(10,20)

    Utils.testA += 1  #相当于给全局变量赋值了

    study14.testA_func() # 其他文件里的同一个变量也变化了  102

    print "study15 Utils.testA", Utils.testA   # 102


    # 创建对象
    UF = MathUtils()
    UF._testA += 1
    print UF.add(1,3), UF._testA

    UF1 = MathUtils()

    print UF1.add(1, 4), UF1._testA  #实例对象相互不影响

if __name__ == "__main__":

    module_func()



