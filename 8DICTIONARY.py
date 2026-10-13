#字典可以通过key找value，key原则上不可以重复，否则两个相同的key只会对应最新的value
#字典不支持下标索引，可以修改

my_dict={"zhangsan":89,"lisi":60,"wanwu":100}
my_dict2={}#空字典
my_dict3=dict()#空字典
print(f"my_dict的内容是{my_dict}，数据类型为{type(my_dict)},my_dict2的数据内容：{my_dict2}")

score=my_dict["zhangsan"]
print(f"zhangsan 的成绩为：{score}")

#二维字典
students_score_dict={
    "zhangsan":{
        "chinese":68,
        "math":89,
        "english":97
    },
    "lisi":{
        "chinese":56,
        "math":76,
        "english":43
    },
    "wangwu":{
        "chinese":89,
        "math":90,
        "english":100
    },
}
print(f"所有学生的考试信息为：{students_score_dict}")
print(f"zhangsan的语文信息为:{students_score_dict['zhangsan']['chinese']}")

#字典新增元素
my_dict["zhaoliu"]=99
print(f"新增元素后的my_dict:{my_dict}")

#字典修改元素
my_dict["zhangsan"]=96
print(f"修改zhangsan后的my_dict:{my_dict}")

#字典删除元素
deleted_value=my_dict.pop("lisi")
print(f"删除后的my_dict:{my_dict}，删除的值为：{deleted_value}")

#清空dict
my_dict.clear()
print(f"清除后的my_dict:{my_dict}")

#获取全部的key
my_dict={"zhangsan":89,"lisi":60,"wanwu":100}
keys=my_dict.keys()
print(f"全部key为“{keys}")

#遍历字典（对key进行遍历）
for _ in keys:
    print(f"字典的key是：{_}")
    print(f"字典的value是：{my_dict[_]}")
    
#法2：直接对字典遍历
for _ in my_dict:
    print(f"法2字典的key是：{_}")
    print(f"法2字典的value是：{my_dict[_]}")

#统计元素数量
print(f"字典my_dict的元素数量为：{len(my_dict)}")