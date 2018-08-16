# #_*_ coding:utf-8 _*_



def input_fun():

    # raw_input() 将所有输入作为字符串看待，返回字符串类型。
    #i nput( ) 只能接收“数字”的输入，在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）。

    print "How old are you? "
    age = raw_input() # 返回的是字符串

    print "How tall are you? "
    heigt = raw_input()

    print "age is %s, height is %s" % (age, heigt)

    str = raw_input("请输入：")

    print str

    age1 = input()
    heigt1 = input()

    print "age1 is %d, height1 is %f" % (age1, heigt1)





if __name__ == "__main__":
    input_fun()