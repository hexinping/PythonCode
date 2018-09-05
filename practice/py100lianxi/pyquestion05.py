# -*- coding: UTF-8 -*-

'''

    题目：输入三个整数x,y,z，请把这三个数由小到大输出。

    程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
    然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
'''


def compare_ele(element):
    return element.value


#这个是按照key值排序
def sortedDictValues1(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]

def func1():

    # a = int(raw_input(">"))
    # b = int(raw_input(">"))
    # c = int(raw_input(">"))

    # 使用默认的排序
    # arr = []
    # arr.append(a)
    # arr.append(b)
    # arr.append(c)

    # arr1 = arr.sort() #不会产生新的列表 arr1为None,修改的是原有列表
    #
    # print arr
    # print arr1  #输出为None
    #
    # arr2 = sorted([a,b,c]) #产生新的列表 arr2不为None
    # print arr2


    #用自定义函数排序 使用sort的key关键字

    # arr = []
    # t1 = {"1":a}
    # arr.append(t1)
    # t2 = {"2": b}
    # arr.append(t2)
    # t3 = {"3": c}
    # arr.append(t3)

    # arr.sort(key = compare_ele)

    # print arr


    #这个是按照key值排序
    test = {"2":1,"3":33,"4":2}
    items = test.items()
    items.sort()

    test1 = [value for key, value in items]

    print test1











if __name__ == "__main__":
    print "05--------"

    func1()