# #_*_ coding:utf-8 _*_





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



def dictionary_func():

    states = {
        "or": 1,
        "and":2,
        "yes":3,
        "no":4
    }

    print states["or"]

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


if __name__ == "__main__":

    list_func()

    # dictionary_func()