print("===============对象=================")
class Student:
    name=None
    gender=None
    nationality=None
    native_place=None
    age=None

#创建对象
stu1=Student()

#对象赋值
stu1.name="林俊杰"
stu1.gender="male"
stu1.nationality="China"
stu1.native_place="shandong Privince"
stu1.age=31

print(type(stu1))
print(stu1.age)
print()


print("===============成员方法=================")
class Person:
    name=None
    #类里面的函数叫方法
    #self表示类对象的本身，只有通过self，成员方法才能访问类的成员变量
    #self不占用形参位置，无需理会
    def say_hi(self):
        print(f"大家好，我是{self.name}")
    def say_hi2(self,msg):
        print(f"大家好，我是{self.name},{msg}")

per1=Person()
per1.name="周杰伦"
per1.say_hi()
per1.say_hi2("请多多关照")

print("===============类和对象=================")

class Clock:
    id=None
    price=None
    def ring(self):
        import winsound
        print("ring!ring!irng!")
        #winsound.Beep(2000,3000)
        
clock1 = Clock()
clock1.id="1234"
clock1.price=20
print(f"闹钟ID为：{clock1.id},价格：{clock1.price}")
clock1.ring()

print("===============构造方法+魔术方法=================")
class Worker:
    #这个方法不仅可以定义，还可以赋值，可以舍去name=None,age=None...
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
        print("Worker类创建了一个类对象")
    #__str__魔术方法
    def __str__(self):
        return f"Worker类对象，name：{self.name},age:{self.age},telephone:{self.tel}"
        
    #__lt__魔术方法
    def __lt__(self,other):
        return self.age<other.age
    
    #__le__
    def __le__(self,other):
        return self.age<=other.age
    
    #__eq__
    def __eq__(self,other):
        return self.age==other.age
    
    
w1=Worker("蔡徐坤",35,"10086")
w2=Worker("林俊杰",43,"10086")
print(w1.name)
print(w1.age)
print(w1.tel)
print(w1)#使用__str__()后，print(w1)输出的不再是w1的内存地址，而是指定的格式
print(w1<w2)#__lt__
print(w1>=w2)#__le__
print(w1==w2)#__eq__

print("===============封装=================")

class Phone:
    #以两个下划线写的变量或方法是私有的，
    #类对象无法访问私有成员，类中的其他成员可以访问私有成员
    __current_voltage=0.1
    def __keep_single_core(self):
        print("CPU以单核运行")
        
    def call_by_5g(self):
        if self.__current_voltage>=1:
            print("5G通话开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5G通话")
phone=Phone()
phone.call_by_5g()

print("===============继承=================")

class old_Phone():
    IMEI=None
    producer="appa"
    
    def call_by_4G(self):
        print("4G通话")
    
class new_Phone(old_Phone):#new继承了old的变量和方法
    face_id="10001"
    
    def call_by_5G(self):
        print("5G通话")
        
phone1=new_Phone()
print(phone1.producer)
phone1.call_by_4G()
phone1.call_by_5G()

#多继承
class NFCReader():
    nfc_type="第5代"
    producer="viva"
    
    def read_card(self):
        print("NFC读卡")
        
    def write_card(self):
        print("NFC写卡")
        
class RemoteControl():
    rc_type="红外遥控"
    
    def control(self):
        print("红外遥控开启")
        

class MyPhone(new_Phone,NFCReader,RemoteControl):
    pass#只继承了这三个功能，没有添加新功能

myphone=MyPhone()
myphone.call_by_4G()
myphone.read_card()
myphone.write_card()
myphone.control()
print(myphone.producer)#new_Phone比NFCReader先被继承，优先new_Phone的producer

print("===============复写=================")
class Fixed_Phone(old_Phone):#继承old_Phone
    producer="大米"#复写producer
    
    def call_by_4G(self):#复写call_by_4G
        print("更省电的4G通话")
        
        '''调用父类方式1'''
        # print(f"父类厂商为：{old_Phone.producer}")
        # old_Phone.call_by_4G()
        
        '''调用父类方式2'''
        print(f"父类厂商为：{super().producer}")
        super().call_by_4G()
        
        
myphone2=Fixed_Phone()
myphone2.call_by_4G()
print(myphone2.producer)

print("===============多态=================")

class Animal():
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        print("wolf wolf wolf")

class Cat(Animal):
    def speak(self):
        print("mew mew mew")
        
def make_noise(animal:Animal):
    animal.speak()

dog=Dog()
cat=Cat()

#多态：同样的行为，使用不同的对象，获得不同的运行状态
make_noise(dog)
make_noise(cat)