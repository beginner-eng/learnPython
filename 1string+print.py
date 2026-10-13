name="programmer"#str
gender='man'
age=20.1234#float
salary=1234#int

print(type(age))#输出age的数据类型
print(int(age))#将age转换为int型

#3 ways to print information
print(name,gender,age,salary)#用','隔离各个数据
print(name+gender)# str拼接用+
print("There is a guy,his name is %s,\nhis gender is %s,\nage is %5.3f,\nsalary is %d\n\n"%(name,gender,age,salary))

#这种方法不能精度控制
print(f"There is a guy called {name},he is a {gender},he is {age} years old")