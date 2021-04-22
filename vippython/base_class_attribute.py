class People:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #不希望在类外部使用，在参数之前加上__


'''封装'''
p=People('liujy',10);
# print(p.__age) #报错不能使用
# print(dir(p))
print(p._People__age) #如果真的想使用也可以用这个方法


'''继承 python支持多继承'''
class Student(People): #student继承People
    def __init__(self,name,age,stuno):
       super().__init__(name,age)
       self.stuno=stuno

'''特殊属性和特殊方法'''
print(dir(object))
stu=Student('ljy',10,1)
print(stu.__dict__)  #{'name': 'ljy', '_People__age': 10, 'stuno': 1} 实例对象的属性字典
print(stu.__class__) #<class '__main__.Student'>
print(Student.__bases__) #(<class '__main__.People'>,) 输出类的所有父类的元组
print(Student.__base__) #<class '__main__.People'> 输出最近的父类
print(Student.__mro__) #(<class '__main__.Student'>, <class '__main__.People'>, <class 'object'>) 输出类的层次结构

'''如果想两个对象相加  可以使用__add__ 方法'''
'''__len__'''

'''浅拷贝 深拷贝'''


import math
print(math.pi)

'''或者使用 from math import pi'''


'''以主程序形式运行'''

if __name__=='__main__':
    print(111)    #如果这个模块被import了，在引用的文件不会输出这一段，只有在单独运行这个模块才可以运行这一段


