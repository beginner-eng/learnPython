'''================文件读取================='''
#使用open打开一个文件
f=open("E:/code/Python_Program/learnPython/TestText.txt","r",encoding="UTF-8")
print(f"文件为：\n{f};\n文件类型为:\n{type(f)}\n")

#read(num)   num表示从文件中读取的数据长度（单位字节），如果没有num参数，则读取所有数据
text1=f.read(30)
print(f"文件前30个字节内容为：\n{text1}\n文件类型为:\n{type(text1)}\n")

#readlines()   读取整个文件，并返回一个列表，每一行的数据作为一个元素
text2=f.readlines()
print(f"文件内容为：\n{text2}\n文件类型为:\n{type(text2)}\n")

#readline每一次只读取一行，调用一次往下移动一行，这里上面代码已经把文件读取完了，所以这里没有内容，可以将其注释掉
line1=f.readline()
line2=f.readline()
line3=f.readline()
print(f"第一行数据为：{line1}")
print(f"第二行数据为：{line2}")
print(f"第三行数据为：{line3}")

for line in f:
    print(f"每一行数据是：{line}")
    
#程序结束一定要关闭文件
f.close()

#这个句式可以调用完成之后自动关闭文件
with open("E:/code/Python_Program/learnPython/TestText.txt","r",encoding="UTF-8") as f1:#这个f1相当于上面的f
    for line in f1:
        print(f"每一行数据是：{line}")
        

