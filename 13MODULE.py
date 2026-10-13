#导入语法如下：
#  [from 模块名] import [ 模块 | 类 | 变量 | 函数 | *] [as 别名]


# import time#可以使用time的所有功能
# print("begin:\nwait for a second")
# time.sleep(3)    #需要用time.引出函数
# print("finished")


# from time import sleep
# print("begin:\nwait for a second")
# sleep(3)    #直接使用sleep，不用time.引出
# print("finished")


# from time import *        #引入所有功能，且不用time.引出
# print("begin2:\nwait for a second")
# sleep(3)
# print("finished2")

from time import sleep as sl   #给sleep取名为sl
print("begin2:\nwait for a second")
sl(3)
print("finished2")