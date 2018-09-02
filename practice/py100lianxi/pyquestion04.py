# -*- coding: UTF-8 -*-

'''
    题目：输入某年某月某日，判断这一天是这一年的第几天？

    程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
            特殊情况，闰年且输入月份大于2时需考虑多加一天

'''

def isRunYear(year):
    x = year
    if x % 4 == 0 and x % 100 != 0:
        return True
    elif x % 400 == 0:
        return True
    else:
        return False

def getDaysWithMonth(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return  30

def getTotalDaysWithMonth(month):

    total = 0
    while month > 0:
        total += getDaysWithMonth(month)
        month = month - 1

    return total



def func():

    year = int(raw_input('please enter a year:'))

    month = int(raw_input('please enter a month:'))
    day = int(raw_input('please enter a day:'))

    runYear = isRunYear(year)

    totalDays = day + getTotalDaysWithMonth(month-1)

    if runYear:
        totalDays += 1
    print "今年已经过了:%d" % totalDays


def func2():
    year = int(raw_input('year:\n'))
    month = int(raw_input('month:\n'))
    day = int(raw_input('day:\n'))

    #前几个月累计的天数
    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    if 0 < month <= 12:
        sum = months[month - 1]
    else:
        print 'data error'
    sum += day
    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1

    if (leap == 1) and (month > 2):
        sum += 1
    print 'it is the %dth day.' % sum

if __name__ == "__main__":
    print "04----------"
    func()
    func2()