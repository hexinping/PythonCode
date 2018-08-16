
# #_*_ coding:utf-8 _*_


def varsName():

    '''

    命令方式用下划线或者驼峰都可以吧
    操作符两边加上空格易于阅读

    '''

    cars = 100
    space_in_a_car = 4.0
    drivers = 30
    passengers = 90
    cars_not_driven = cars - drivers
    cars_driven = drivers
    carpool_capacity = cars_driven * space_in_a_car
    average_passengers_per_car = passengers / cars_driven

    print "There are", cars, "cars available."
    print "There are only", drivers, "drivers available."
    print "There will be", cars_not_driven, "empty cars today."
    print "We can transport", carpool_capacity, "people today."
    print "We have", passengers, "to carpool today."
    print "We need to put about", average_passengers_per_car, "in each car."


def printFormat(name, age):

    #   %是用与连接格式符号的
    print "name is %s" % name, " age is %d" % age


if __name__ == "__main__":

    varsName()

    printFormat("hexinping", 23)



