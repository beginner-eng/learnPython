'''================文件写出================='''

''' ✔ Windows 路径尽量用 r"..."   在前面加 r,让 Python 不解析反斜杠。
    ✔ 或者用 /     正斜杠
    ✔ 或者用 \\    双反斜杠'''
#创建一个TestOut的txt文件,这里我在路径前面加r，路径直接复制系统路径，比较方便
#注意，w模式如果文件存在，写入的内容则会覆盖原文件内容
f=open(r"E:\code\Python_Program\learnPython\TestOut.txt",'w',encoding='UTF-8')
#写入
f.write("hello world!!!")
#刷新，将内存中的内容写入到硬盘中的文件
f.flush()
#关闭程序，其实close内置了flush方法，可以将flush注释掉
f.close()