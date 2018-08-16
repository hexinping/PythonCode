# #_*_ coding:utf-8 _*_


# 函数外部的变量属于全局变量
age = 12
height = 1.78

def local_vars(var1, var2):
    """
        这些变量是在函数之外的，当它们被传递到函数中以后，函数会为这些变量创建一些临时的
        版本，当函数运行结束后，这些临时变量就被丢弃了，一切又回到了从前
    """

    # 定义在函数内部的都是局部变量
    age = 21
    height = 2.45

    #在函数内部使用全局变量 并改变全局变量
    # """
    #     global age
    #     age = 27
    # """



    print "var1 %r, var2 %r" % (var1, var2)
    print "local_age %r, local_height %r" % (age, height)

if __name__ == "__main__":

    local_vars(age,height)

    print "age %r, height %r" % (age, height)