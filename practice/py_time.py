# -*- coding: UTF-8 -*-

'''
    https://www.cnblogs.com/renpingsheng/p/6965044.html
    http://www.runoob.com/python/python-date-time.html
    https://blog.csdn.net/you_are_my_dream/article/details/61616465
    time模块提供各种时间相关的功能

    这个模块的功能不是适用于所有的平台
    这个模块中定义的大部分函数是调用C平台上的同名函数实现??? c不是跨平台的吗

'''

import  time

def time_func():
    # time.altzone
    # 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。

    print time.altzone

    # time.asctime([tupletime])
    # 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日周二18时07分14秒）的24个字符的字符串。

    print time.asctime()

    #time.localtime([secs])：将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。

    struct_time1 = time.localtime()  #返回当前时区的当前时间
    struct_time2 = time.localtime(1304575584.1361799)

    print struct_time1.tm_year,struct_time1.tm_mon,struct_time1.tm_mday,
    print struct_time1.tm_hour,struct_time1.tm_min,struct_time1.tm_sec

    #time.gmtime([secs])：和localtime()方法类似，
    # gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。

    print time.gmtime()

    #time.time()：返回当前时间的时间戳。
    print time.time()

    #time.mktime(t)：将一个struct_time转化为时间戳。
    print time.mktime(time.localtime())


    #time.clock()
    '''
        其中第一个clock()输出的是程序运行时间
        第二、三个clock()输出的都是与第一个clock的时间间隔
    '''
    time.sleep(1)
    print "clock1:%s" % time.clock()
    time.sleep(1)
    print "clock2:%s" % time.clock()
    time.sleep(1)
    print "clock3:%s" % time.clock()

    # time.ctime()把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。
    print time.ctime()


    '''
        time.strftime(format[, t])：把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一个元素越界，ValueError的错误将会被抛出。
    '''

    print  time.strftime("%Y-%m-%d %X", time.localtime())

if __name__ == "__main__":
    print "time-----"

    time_func()