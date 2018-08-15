# #_*_ coding:utf-8 _*_


# 导入自定义模块
import Utils


def user_defined():

    #使用Utils模块里的add方法 Utils.add
    sum = Utils.add(3, 4)
    print "sum %d" % sum


if __name__ == "__main__":

    user_defined()

