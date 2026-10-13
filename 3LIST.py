#list 里面的数据类型可以多种多样，也支持嵌套(其实就是里面的元素数据类型可以支持其本身)，python太强了
my_list=['zhangsan',[1,3,True],'wangwu',None,'qianqi',['hello',3.14]]
print(my_list)
print(my_list[1][2])#取出True
print(my_list[-1][-1])#取出3.14,序号可以为负数


print(f"获取存在的元素[1,3,True]的索引：{my_list.index([1,3,True])}")#获取元素索引
#print(f"获取不存在的元素\"hello\"的索引：{my_list.index("hello")}")#获取不存在元素会报错

my_list[1][2]=False#修改元素的值
print(my_list)

#插入元素，把二号元素及其以后的元素下标加1，空出的二号添加插入的新元素
my_list.insert(2,"Im_insert")
print(my_list)

#追加元素，将想要追加的元素添加到list末尾
my_list.append("Im_append")
print(f"\n追加了一个新元素Im_append后的list：\n{my_list}")

#extend将其他 容器 的元素直接加到引用者的末尾
my_list2=[1,3,False]
my_list.extend(my_list2)
print(f"\n将其他容器的元素添加到mylist后：\n{my_list}")

#删除元素
del my_list[1]
print(f"\n删除my_list[1]后的mylist:\n{my_list}")

#删除元素方法2，pop删除指定下标的元素，还可以返回被删除的元素的值
deleted_element=my_list.pop(5)
print(f"\n删除下标5的{deleted_element}后的mylist为：{my_list}\n")

#删除元素方法3，可以不用知道元素下标，知道元素的值的时候使用
#注意如果list中有两个相同的元素，此方法只会删除第一个(因为此方法为是顺序查找)
my_list.remove("zhangsan")
print(f"\n删除指定元素\"zhangsan\"后的list：\n{my_list}")

#清空列表
my_list.clear()
print(f"\n清空后的list:\n{my_list}")

my_list.append(1)
my_list.append(1)
my_list.append(2)
my_list.append(3)
number=my_list.count(1)
#统计list中的某元素的数量
print(f"\nlist中元素1的数量为：{number}")

length=len(my_list)
print(f"\nlist的长度为：{length}")

#遍历list
for element in my_list:
    print(f" 元素有 {element} ",end='')