class Student: #类名是有一个或者多个单词组成，每个单词的首字母一定要大写其余小写
    class_param='liujy'  #类属性
    # age=27
    def __init__(self,name,age):
        self.name=name  #self.name 叫做实例属性，将局部变量赋给实例属性
        self.age=age
    def eat(self):  #实例方法
        print('正在吃饭')

    @staticmethod
    def method():
        print('静态方法')

    @classmethod
    def out(cls):
        print('类方法')





def drink():
    print('正在喝')



print(type(Student)) #<class 'type'>
stu=Student('liujy',18)
stu.eat()
print(stu.age)
print(stu.name)
#实例方法调用 可以用（1）对象.方法名（）   （2）类名.方法名（对象）
Student.eat(stu)
print(stu.class_param)  #调用类属性
