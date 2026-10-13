#元组像列表，但不可被修改(但如果元组的元素有list，则list中的元素可以被修改)，所以不能用append pop等操作
my_tuple=(1,"hello",True)
tuple2=()#定义一个空元组
print(f"my_tuple的类型为{type(my_tuple)},内容为{my_tuple}")
t3=((1,2),(3,4,5),6,7,8,8,[9,10,11])
print(t3)
print(t3[1][2])
print(t3.index((3,4,5)))
print(t3.count(8))
print(len(t3))
t3[6][1]=100
print(t3)