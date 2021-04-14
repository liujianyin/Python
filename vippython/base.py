#保留字
import keyword;
print(keyword.kwlist);

#输出变量存放在内存的id值和变量的类型
name='liujy';
print(id(name));
print(type(name));
print(name)

name='hk';
print(id(name));
print(type(name));
print(name)

#数据类型

'''input函数，用户交互 '''
# present=input('what do you want?');
# print(present,type(present));

# a=input('请输入一个整数');
# b=input('输入另一个整数'); #输入的值被默认类型是str
# print('结果是',int(a)+int(b));

#算数运算符
#幂运算
print(2**3)  #8


'''python 牛逼'''
a,b,c=1,2,3
print(a,b,c)
a,b,c=c,b,a
print(a,b,c)


'''is是比较的是id值，对于下面赋值，变量的id值是一致的，内存空间在赋值b的时候会去检测有没有10 的内存
空间，如果有会直接将a指向b，所以导致a,b的id值是一致的'''
d=10
e=10
print(d is e)

'''对于 is 和 is not的比较永远比的内存id一致'''

'''布尔运算符 and or not in not in '''
f=True
print(not f )

g='hello'
print('a' in g)  #false
print('a' not in g) #true
