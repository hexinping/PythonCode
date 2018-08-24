# -*- coding: UTF-8 -*-


import  datetime
import  time

def datetime_func():

    # print datetime.datetime
    # print datetime.date
    # print datetime.time
    # print datetime.timedelta

    #获取当前datetime
    dt = datetime.datetime
    print dt.now()

    #获取当天date
    print datetime.date.today()

    # 获取明天/前N天
    print datetime.date.today() + datetime.timedelta(days=1)
    print datetime.date.today() - datetime.timedelta(days=3)

    #获取当天开始和结束时间(00:00:00 23:59:59)
    print datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    print datetime.datetime.combine(datetime.date.today(), datetime.time.max)

    #获取两个datetime的时间差
    print (datetime.datetime(2015,1,13,12,0,0) - datetime.datetime.now()).total_seconds()


    #datetime <=> string
    print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #string -> datetime
    print datetime.datetime.strptime("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S")

    #datetime <= > timetuple
    print datetime.datetime.now().timetuple()

    #datetime <=> date
    print datetime.datetime.now().date()

    #date -> datetime
    today = datetime.date.today()
    print today
    print datetime.datetime.combine(today, datetime.time())
    print datetime.datetime.combine(today, datetime.time.min)


    #datetime <=> timestamp
    now = datetime.datetime.now()
    timestamp = time.mktime(now.timetuple())
    print timestamp

    #timestamp -> datetime
    print datetime.datetime.fromtimestamp(1421077403.0)



if __name__ == "__main__":
    print "datetime----------"
    datetime_func()