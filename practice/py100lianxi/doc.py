# -*- coding: UTF-8 -*-

'''

1 range(N)：0~N-1    range(M,N): M~N-1

2 list.sort(cmp=None, key=None, reverse=False)
cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。

    # 获取列表的第二个元素
    def takeSecond(elem):
        return elem[1]

    # 列表
    random = [(2, 2), (3, 4), (4, 1), (1, 3)]

    # 指定第二个元素排序
    random.sort(key=takeSecond)

    # 输出类别
    print '排序列表：', random

cmp参数不怎么用，因为key和reverse比单独一个cmp效率要高。

如果进行降序排列，只需要加上reverse=True

总结： sorted 和list.sort 都接受key, reverse定制。但是区别是。list.sort()是列表中的方法，只能用于列表。而sorted可以用于任何可迭代的对象。
list.sort()是在原序列上进行修改，不会产生新的序列。所以如果你不需要旧的序列，可以选择list.sort()。
sorted() 会返回一个新的序列。旧的对象依然存在。


'''
