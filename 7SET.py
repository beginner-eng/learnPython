#集合不允许重复，zhangsan和lisi只会在print里面出现一次，且顺序无法保证
#因为集合无序，所以不支持下标访问
my_set={"zhangsan","lisi","zhangsan","lisi","wangwu","zhaosi","qianqi"}
empty_set=set()
print(f"my_set的内容是{my_set}，类型是{type(my_set)}empty_set的内容是{empty_set}")

#add添加新元素到set里面
my_set.add("python")
print(f"my_set添加python后：{my_set}")

#remove移除元素
my_set.remove("qianqi")
print(f"移除\"qianqi\"后的my_set:{my_set}")

#pop随机取出一个元素
poped_elem=my_set.pop()
print(f"取出{poped_elem}后的my_set为：{my_set}")

#clear清空
cleared_set=my_set.clear()
print(f"清除后的set为{my_set}")

#   集合1.difference(集合2)     取出集合1和集合2的差集(集合1有而集合2没有的！！！)
set1={1,2,3,4,5,6}
set2={3,4,5,6,7}
set3=set1.difference(set2)#不包括7，因为输出集合1有而集合2没有的！！！
print(f"集合1和2的差别是：{set3}")

#集合1.difference_update(集合2)     在集合1内，删除和集合2 相同的元素(集合1被修改)
set1.difference_update(set2)
print(f"消除差集后，集合1的内容：{set1}")


#union将两集合组合成一个新集合
set3=set1.union(set2)
print(f"将两集合合并后：{set3}")

#len统计集合元素数量
print(f"set1的长度为：{len(set1)}")

#遍历集合
print("集合2的元素有：",end='')
for _ in set2:
    print(f"{_} ",end='')