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
• raise   $$$$$$  用raise语句自己触发异常
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
    # 由于python都是引用，而python有GC机制，所以，del语句作用在变量上，而不是数据对象上。

    a = 1  # 对象 1 被 变量a引用，对象1的引用计数器为1
    b = a  # 对象1 被变量b引用，对象1的引用计数器加1
    c = a  # 1对象1 被变量c引用，对象1的引用计数器加1
    del a  # 删除变量a，解除a对1的引用
    del b  # 删除变量b，解除b对1的引用
    print(c)  # 最终变量c仍然引用1
    # print(a)      报错 local variable 'a' referenced before assignment

    # del删除的是变量，而不是数据

    li = [1, 2, 3, 4, 5]  # 列表本身不包含数据1,2,3,4,5，而是包含变量：li[0] li[1] li[2] li[3] li[4]
    first = li[0]  # 拷贝列表，也不会有数据对象的复制，而是创建新的变量引用
    del li[0]
    print(li)  # 输出[2, 3, 4, 5]
    print(first)  # 输出 1


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
    # https://www.cnblogs.com/DswCnblog/p/6126588.html

    with open("config/copy.txt") as file:
        data = file.read()

    # 基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
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


def assert_func():
    # assert condition
    '''
    用来让程序测试这个condition，如果condition为false，那么raise一个AssertionError出来。逻辑上等同于：

    if not condition:
        raise AssertionError()
    '''

    assert 1 == 1  # 条件为false才报错
    assert 1 == 0


def pass_func():
    '''
     Python pass是空语句，是为了保持程序结构的完整性。
         pass 不做任何事情，一般用做占位语句
    '''

    for letter in 'Python':
        if letter == 'h':
            pass
            print '这是 pass 块'
        print '当前字母 :', letter

    print "Good bye!"


# https://blog.csdn.net/u013205877/article/details/70332612
# http://www.runoob.com/w3cnote/python-yield-used-analysis.html
# yield 优点：减少内存占用以及代码简洁
def yield_func():
    '''
        通常的for…in…循环中，in后面是一个数组，这个数组就是一个可迭代对象，类似的还有链表，字符串，文件。它可以是
        mylist = [1, 2, 3]，也可以是mylist = [x*x for x in range(3)]。
        它的缺陷是所有数据都在内存中，如果有海量数据的话将会非常耗内存。

    '''

    def yield_test(n):
        for i in range(n):
            '''
                yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面的值。
                重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码开始执行

                简要理解：yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后开始。
            '''
            yield i  # 这里直接返回i
            print "i=", i

    for x in yield_test(5):
        print x, ","

    '''
        send(msg)与next()的区别在于send可以传递参数给yield表达式，这时传递的参数会作为yield表达式的值，
        而yield的参数是返回给调用者的值。换句话说，就是send可以强行修改上一个yield表达式值。

        比如函数中有一个yield赋值，a = yield 5，第一次迭代到这里会返回5，a还没有赋值。
        第二次迭代时，使用.send(10)，那么，就是强行修改yield 5表达式的值为10，本来是5的，那么a=10
    '''

    def fun111():
        for i in range(20):
            x = yield i
            print('good', x)

    a = fun111()
    b = a.next()  # 这里会直接返回第一个i值，就是0
    print "b--", b
    x = a.send(5)  # 这里会从上一直yield处执行直接修改func111中x的值，但是返回i的值1，所以x为1
    print "x--", x


# 异常处理
# http://www.runoob.com/python/python-exceptions.html
def except_func():
    '''

    异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。
    一般情况下，在Python无法正常处理程序时就会发生一个异常。
    异常是Python对象，表示一个错误。
    当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。

    '''

    '''
        捕捉异常可以使用try/except语句。
        try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
        如果你不想在异常发生时结束你的程序，只需在try里捕获它。

        如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，
        控制流就通过整个try语句（除非在处理异常时又引发新的异常）。 

        try:
        <语句>        #运行别的代码
        except <名字>：
        <语句>        #如果在try部份引发了'name'异常
        except <名字>，<数据>:
        <语句>        #如果引发了'name'异常，获得附加的数据
        else:
        <语句>        #如果没有异常发生 

    '''

    try:
        fh = open("testfile", "r")
        fh.write("这是一个测试文件，用于测试异常!!")
    except IOError:
        print "Error: 没有找到文件或读取文件失败"
    else:
        print "内容写入文件成功"
        fh.close()


eval_a = 10


# https://www.cnblogs.com/yangmingxianshen/p/7810496.html
def eval_exec_compile_func():
    # eval函数
    '''
        计算指定表达式的值。
        也就是说它要执行的python代码只能是单个表达式（注意eval不支持任何形式的赋值操作），而不能是复杂的代码逻辑。
        eval(source, globals=None, locals=None, /)


        source：必选参数，可以是字符串，也可以是一个任意的code(代码)对象实例（可以通过complie函数创建）。如果它是一个字符串，它会被当作一个（使用globals和locals参数作为全局和本地命名空间的）python表达式进行分析和解释。
        globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。
        locals：可选参数，表示全局命名空间（存放局部变量），如果被提供，可以是任何映射对象。如果参数被忽略，那么它将会取与globals相同的值。
        如果globals与locals都被忽略，那么它们将取eval()函数被调用环境下的全局命名空间和局部命名空间。

    '''

    x = 20
    y = eval("x + eval_a")

    print "y=%d" % y

    # exec函数
    '''
        动态执行python代码。也就是说exec可以执行复杂的python代码，而不像eval函数那样只能计算一个表达式的值。

        source：必选参数，表示需要被指定的python代码。它必须是字符串或code对象。
        如果source是一个字符串，该字符串会先被解析为一组python语句，然后执行。
        如果source是一个code对象，那么它只是被简单的执行。

        exec函数的返回值永远为None。

        ================================
        eval()函数和exec()函数的区别：
            eval()函数只能计算单个表达式的值，而exec()函数可以动态运行代码段。
            eval()函数可以有返回值，而exec()函数返回值永远为None。
        ================================

    '''

    # a = exec("x + eval_a")


if __name__ == "__main__":
    # del_func()
    # with_as_func()

    # assert_func()

    # pass_func()

    # yield_func()

    # except_func()

    eval_exec_compile_func()

