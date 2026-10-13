'''================文件写出================='''

#创建一个TestOut的txt文件
f=open(r"E:/code/Python_Program/learnPython/TestOut.txt",'w',encoding='UTF-8')
#写入
f.write("hello world!!!")
#刷新，将内存中的内容写入到硬盘中的文件
f.flush()
#关闭程序，其实close内置了flush方法，可以将flush注释掉
f.close()