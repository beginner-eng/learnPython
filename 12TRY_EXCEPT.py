'''==============捕获异常=============='''
try:
    f=open(r"E:\code\Python_Program\learnPython\NotExist.txt",'r',encoding='UTF-8')
    print("文件存在")
except:
    print("文件不存在，我将创建并写入内容")
    f=open(r"E:\code\Python_Program\learnPython\NotExist.txt",'w',encoding='UTF-8')
    f.write("new content")
    f.close()
    
'''==============捕获异常=============='''
try:
    print(name)
except NameError as err:#捕获指定异常NameError，如果print(name)改成a=1/0,程序会报错，不能捕获NameError
    print("出现变量未定义的异常")
    print(err)


try:
    a=1/0
except ZeroDivisionError as err2:#捕获指定异常ZeroDivisionError
    print("除数为0错了")
    print(err2)
    
'''==============捕获多种异常=============='''
try:
    #b=1/0
    print(name)
except (NameError,ZeroDivisionError) as err3:#若出现 可能出现多种异常 的情况，可以将异常类型放入元组
    print("出现 变量未定义 或 除以零 的 错误")
    print(err3)
    
'''==============捕获所有异常=============='''
try:
    #以read模式打开一个不存在的文件
    #f=open(r"E:\code\Python_Program\learnPython\abcd.txt",'r',encoding='UTF-8')
    
    #除0错误
    b=1/0
    
    #变量未定义
    #print(name)
except Exception as err3:#捕获所有异常
    print("\n出现错误为：")
    print(err3)
    
'''==============异常的else和finally用法=============='''
try:
    #print("\nhello")
    a=1/0
except:
    print("\n出现err")
else:#如果执行了except的内容，则不会执行else的内容
    print("很高兴程序没有出现异常\n")
finally:
    print("无论是否异常，我一定会执行\n")
        
'''==============异常的传递性=============='''
def func1():
    print("func1 开始")
    print(1/0)
    print("func1 结束")
    
def func2():
    print("func2 开始")
    func1()
    print("func2 结束")
    
def main():
    try:
        print("main 开始")
        func2()
        print("main 结束")
    except Exception as e:
        print(f"出现异常，类型为:{e}")
main()