print("========基础数据类型注解=========")
import json
import random


val_1:int=10#val_1是int型
val2:str="hello"#val2是str型
val3:bool=True

class Student():
    pass
stu1:Student=Student()

my_list:list[int]=[1,2,3]#list里面存的都是整型
my_tuple:tuple[int,str,bool]=(2,"caixvkun",True)#元组类型需要将每个元素类型都标注出来
my_dict:dict[str,int]={"id":1234}#字典类型需要标注key和value

print("========在注释中进行类型注释(真管用，会解析)=========")
val4=random.randint(1,10)    # type: int
val5=json.loads('{"name":"zhangsan"}')  #type: dict[str,str]

def func():
    return 10
val6=func() # type: int

print("========函数和方法类型注解=========")
#参数类型注解
def add(x:int,y:int):
    return x+y
print(add(2,3))

#返回值注解
def add_all(data:list) -> int:
    sum=0
    for _ in data:
        sum+=_
    return sum

print(add_all([1,2,3,4,5,6,7,8]))

print("========函数和方法类型注解=========")
from typing import Union
my_list1:list[Union[int,str]]=[1,2,3,"string","name"]#list里可能出现int和str型

def func3(data:Union[int,str]) -> Union[int,str]:
    pass

func3()#鼠标指向括号中间，按下Ctrl+P,会弹出输入参数和返回值的数据类型
