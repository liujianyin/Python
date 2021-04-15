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
print(d is e)  #true

'''对于 is 和 is not的比较永远比的内存id一致'''

'''布尔运算符 and or not in not in '''
f=True
print(not f )

g='hello'
print('a' in g)  #false
print('a' not in g) #true


'''if  else'''
# money=int(input('输入钱数'))
# if money>=100:
#     print('这是一笔大钱')
# else:
#     print('这是一笔小钱')

# score=int(input('请输入成绩数'))
# if score<=0 or score>100:
#     print('非法数据')
# elif score<=50:
#     print('e')
# elif score<=69:
#     print('d')
# elif score<=79:
#     print('c')
# elif score<=89:
#     print('b')
# elif score<=100:
#     print('a')
#

# vipflag=input('是否是会员y/n')
# money=float(input('金额是多少'))
# if vipflag=='y':
#     print('会员')
#     if money>=200:
#         print('付款金额：',money*0.8)
#     elif money>=100:
#         print('付款金额：',money*0.9)
#     else:
#         print('付款金额：', money)
# else:
#     print('不是会员')
#     if money>=200:
#         print('付款金额：',money*0.95)
#     else:
#         print('付款金额：', money)

'''条件表达式'''
# number1=int(input('输入第一个整数'))
# number2=int(input('输入第二个整数'))
# print(str(number1)+'大于等于'+str(number2)  if number1>=number2 else  str(number1)+'小于'+str(number2) )
# print(str(number1),'大于等于',str(number2)  if number1>=number2 else  str(number1),'小于',str(number2) )


'''range'''
numbers=range(2,40,10)
print(numbers)
print(list(numbers))
numbers1=range(20)
print(list(numbers1))

'''while'''
i=0
sum1=0
while i<=100:
    sum1+=i
    i=i+2
print(sum1)


'''for in'''
all=0
for j in range(0,101,2):
    all+=j
print(all)
'''如果在循环体中不需要使用自定义边框，可以将自定义变量写成‘_’'''
# for _ in range(10):
#         print('111')

'''打印出水仙花数'''
count=0
for l in range(100,999):
    sum_=0
    o=l
    while(o!=0):
        m=o%10
        o=int(o/10)
        sum_+=m**3
    if(sum_==l):
        print(sum_)
        count+=1

print(count)


'''for 和 else  搭配使用'''
for _ in range(1,4):
    pwd=input('输入密码')
    if(pwd=='8888'):
        print('密码输入正确')
        break
    else:
        print('密码错误请重新输入')
else:
    print('3次机会已用完')
