# #_*_ coding:utf-8 _*_


def print_format():

    '''

    % 格式化字符串拼接用
    %r 什么都输出 等价于%d %s ...
    
    '''

    name = 'Zed A . show'
    age = 23
    height = 74
    weight = 180
    eyes = 'Blue'
    hair = 'Brown'

    print "Let's talk about %s." % name
    print "He's %d inches tall." % height
    print "He's got %s eyes and %s hair." % (eyes, hair)
    print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
    print "I also said: '%s'." % age

# 英寸转化成厘米
def in_to_cm(i):
    single = 2.54
    return single * i


def lb_to_kg(kg):
    single = 0.4535924
    return kg * single


def inln_to_cmkg(in_value, lb_value):

    cm_value = in_to_cm(in_value)
    kg_value = lb_to_kg(lb_value)

    print "%d in to %f cm" % (in_value, cm_value), "%d lb to %f kg" % (lb_value, kg_value)


def print_plus_format(w, s):
    #两个字符串连接起来，组建成一个新的字符串
    print w + s


def print_in_oneline():

   # print 后加,就可以一行输出

   print "1",
   print "2"


def print_zhuanyi():

    print "hhh '3\" "



if __name__ == "__main__":

    print_format()
    inln_to_cmkg(1, 1)
    inln_to_cmkg(1, 1)
    print_plus_format("2222", "/444")
    print_in_oneline()
    print_zhuanyi()



