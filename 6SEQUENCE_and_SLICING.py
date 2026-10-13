my_list=[1,2,3,4,5,6,7,8,9]
result1=my_list[1:4]#切片从1开始，4结束，默认step为1
print(result1)

my_tuple=(1,2,3,4,5,6)
result2=my_tuple[:]#从头到尾，步长为1可以省略
print(result2)

my_str="123456"
result3=my_str[::2]#从头到尾，步长为2
result4=my_str[::-1]#从头到尾，步长为-1

print(result3)
print(result4)