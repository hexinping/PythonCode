# #_*_ coding:utf-8 _*_


import  Utils

def testA_func():

    Utils.testA += 1

    print "study14 Utils.testA",Utils.testA



def list_func():
    print "hhhhh"


    '''
        stuff[3:5] 实现了什么功能？ ==> stuff[3] stuff[4]
        这是一个列表切片动作，它会从 stuff 列表的第 3 个元素开始取值，直到第 5 个元素。
        注意，这里并不包含第 5 个元素，这跟 range(3,5) 的情况是一样的
    '''

    stuff = "hexinping"

    a = stuff[0]   # h
    b = stuff[3:5] #stuff[3] stuff[4]   in
    c = stuff[5:]  # ping
    print a, b, c

    ######排序

    arr = [1,8,5,9]
    arr1 = [(1,2),(3,11),(2,9)]

    arr_1 = arr.sort() # 使用默认的排序 #不会产生新的列表 arr_1为None,修改的是原有列表
    print arr
    print arr_1

    def cm(element):
        return element[1]

    arr1.sort(key = cm) # 使用自定义的排序
    print arr1



def print_test():
    print "jjjjjj"

def dictionary_func():

    states = {
        "or": 1,
        "and":2,
        "yes":3,
        "no":4
    }

    print states["or"]

    states["age"] = 12 #赋值

    #遍历key值 随机性
    #1
    for key in states:
        print "key1 is %s" % key
    #2
    for key in states.keys():
        print "key2 is %s" % key

    #遍历value值
    for value in states.values():
        print "value is %d" % value

    #遍历字典
    for key,value in states.items():
        print "key is %s" % key, "value is %d" % value


    '''
        1 遍历key值：for key in dict / for key in dict.keys()
        2 遍历value值：for value in dict.values()
        3 遍历整个dict：for key,value in dict.items():
    
    '''


    #获取value值
    a = states["or"]
    b = states.get("and", "not find")

    print a , b



    #字典里存储函数
    states['func'] = print_test

    states['func']()

    # 排序

    t1 = {"a":2,"c":10,"b":3}

    #是按照key值排序
    def sortedDictValues1(adict):
        items = adict.items()
        items.sort()
        return [value for key, value in items]
    t = sortedDictValues1(t1)
    print t

    def sortedDictValues2(adict):
        keys = adict.keys()
        keys.sort()
        return [adict[key] for key in keys]

    t = sortedDictValues2(t1)
    print t

    def sortedDictValues3(adict):
        keys = adict.keys()
        keys.sort()
        return map(adict.get, keys)

    t = sortedDictValues3(t1)
    print t

    #根据value排序
    def sort_by_value(d):
        #先把item的key和value交换位置放入一个list中，再根据list每个元素的第一个值，即原来的value值
        items = d.items()
        backitems = [[v[1], v[0]] for v in items]
        backitems.sort()
        return [backitems[i][1] for i in range(0, len(backitems))]

    t2 = {"a": 20, "c": 10, "b": 3}
    t = sort_by_value(t1)
    print t

if __name__ == "__main__":

    #list_func()

    dictionary_func()