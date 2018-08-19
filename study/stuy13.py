# #_*_ coding:utf-8 _*_


# 关键字
'''
• and
• del    $$$$$$
• from
• not
• while
• as      $$$$$$
• elif
• global  $$$$$$
• or
• with
• assert  $$$$$$
• else
• if
• pass    $$$$$$
• yield   $$$$$$
• break
• except  $$$$$$
• import
• print
• class
• exec    $$$$$$
• in
• raise   $$$$$$
• continue
• finally $$$$$$
• is
• return
• def
• for
• lambda
• try     $$$$$$



'''


def del_func():
    #由于python都是引用，而python有GC机制，所以，del语句作用在变量上，而不是数据对象上。


    a = 1           # 对象 1 被 变量a引用，对象1的引用计数器为1
    b = a           # 对象1 被变量b引用，对象1的引用计数器加1
    c = a           # 1对象1 被变量c引用，对象1的引用计数器加1
    del a           # 删除变量a，解除a对1的引用
    del b           # 删除变量b，解除b对1的引用
    print(c)        # 最终变量c仍然引用1
    # print(a)      报错 local variable 'a' referenced before assignment

    #del删除的是变量，而不是数据

    li = [1, 2, 3, 4, 5]  # 列表本身不包含数据1,2,3,4,5，而是包含变量：li[0] li[1] li[2] li[3] li[4]
    first = li[0]         # 拷贝列表，也不会有数据对象的复制，而是创建新的变量引用
    del li[0]
    print(li)             # 输出[2, 3, 4, 5]
    print(first)          # 输出 1



############################################################


class Sample:
    def __enter__(self):
        print "In __enter__()"
        return "Foo"

    def __exit__(self, type, value, trace):
        print "In __exit__()"


def get_sample():
    return Sample()


class Sample1:
    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        print "type:", type
        print "value:", value
        print "trace:", trace

    def do_something(self):
        bar = 1 / 0  # 故意写错测试
        return bar + 10


def with_as_func():
    #https://www.cnblogs.com/DswCnblog/p/6126588.html

    with open("config/copy.txt") as file:
        data = file.read()

    #基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
    '''
        1. __enter__()方法被执行
        2. __enter__()方法返回的值 - 这个例子中是"Foo"，赋值给变量'sample'
        3. 执行代码块，打印变量"sample"的值为 "Foo"
        4. __exit__()方法被调用
    
    '''

    with get_sample() as sample:
        print "sample:", sample


    '''
        with真正强大之处是它可以处理异常。
        可能你已经注意到Sample类的__exit__方法有三个参数- val, type 和 trace。 
        这些参数在异常处理中相当有用。我们来改一下代码，看看具体如何工作的。

    
    '''

    '''
        在with后面的代码块抛出任何异常时，__exit__()方法被执行。
        正如例子所示，异常抛出时，与之关联的type，value和stack trace传给__exit__()方法，
        因此抛出的ZeroDivisionError异常被打印出来了
    '''
    with Sample1() as sample:
        sample.do_something()



if __name__ == "__main__":

    del_func()
    with_as_func()