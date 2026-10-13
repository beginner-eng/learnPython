'''================函数的多种参数适用形式================'''
def user_info(name,age,gender):
    print(f"名字：{name},年龄：{age},性别：{gender}")

user_info("zhangsan",21,'male')#位置参数，默认使用形式
user_info(name="lisi",age=34,gender='female')#关键字参数
user_info(gender='male',name='wangwu',age=45)#可以不按照参数定义顺序传参
user_info('zhaoliu',gender='male',age=67)

def user_info_v2(name,age,gender='male'):#性别默认为男性，注意：设置了默认值的参数必须排在后面
    print(f"名字：{name},年龄：{age},性别：{gender}")

user_info_v2('zhoujielun',56)#没有传性别，默认为男性

def user_info_v3(*args):#不定长定义的形式参数会作为 元组 存在，接收不定长的参数传入
    print(f"传入的参数类型为:{type(args)}，传入的内容为：{args}")

user_info_v3(1,2,3.14,"xiaoming","小明",False)

def user_info_v4(**kwargs):#传入的不定长参数必须为 dictionary 类型
    print(f"传入的参数类型为:{type(kwargs)}，传入的内容为：{kwargs}")

user_info_v4(name="小帅",age=23,gender='male',addr='beijing')


'''================函数作为参数传递================'''
def test_func(compute,operator1,operator2):#函数可以是一个参数，传入另一个函数进行使用
    result=compute(operator1,operator2)
    print(f"compute参数的类型为：{type(compute)}")
    print(f"结果为：{result}")

def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

test_func(add,3,2)
test_func(multiply,4,5)


'''================lambda匿名函数================'''

#lambda是关键字，格式为lambda 传入参数:函数体      此函数只能调用一次，注意函数体只能写一行！！

def test_func2(comp):
    res=comp(1,2)
    print(f"结果是：{res}")

test_func2(lambda x,y:x+y)
