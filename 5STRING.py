name="programmer and code"

#string可以像列表，元组一样通过下标进行访问
#字符串是一个不可修改的数据容器
for i in name:
    print(f"{i} ",end='')

value=name.index("and")
print(f"\n字符串\"and\"的起始下标为：{value}")

#replace将源字符串1的全部 替换为字符串2，不是修改字符串，而是得到一个新的字符串
new_name=name.replace("code","computer")
print(f"新的名字是： {new_name}")

#split将字符串按照指定的分隔符分割，存入列表
name_list=name.split(" ")
print(f"字符串分割后为：{name_list},类型为：{type(name_list)}")

#strip去除前后指定的字符串
my_str="  an apple and a banana   \n"
new_str=my_str.strip()#默认清除空格和换行
print(f"新字符串为:{new_str},去除了空格")

my_str="21an apple and a banana12"
new_str=my_str.strip('21')
print(f"去除1和2，新字符串为:{new_str},去除了空格")

num=my_str.count('a')
print(f"\n{my_str}中a的数量有{num}个，字符串长度为{len(my_str)}")