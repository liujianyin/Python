def sumNums(a,b):
    c=a+b
    return c

result=sumNums(10,20)
print(result)
result1=sumNums(b=80,a=1) #变量的参数成为关键字参数,不会在乎位置了，传入的值 a 1 b 80
print(result1)

'''如果函数返回值是多个 那返回的是元组'''
def out(a,b):
    return  a,b
print(out(1,23))  #返回的是元组 (1, 23)


'''个数可变的位置参数'''
def fun(*args):   #结果返回元组
    print(args)

fun(1) #(1,)
fun(2) #(2,)
fun(1,2,3) #(1, 2, 3)



'''个数可变的关键字形参'''
def fun1(**args): #返回是个字典
    print(args)

fun1(a='1') # {'a': '1'}
fun1(a='1',b='2') #{'a': '1', 'b': '2'}

'''如果一个函数既有个数可变的关键字形参又有个数可变的位置形参，位置形参要放在关键字形参之前'''
def fun2(*args1,**args2):
    print(args1,args2)

fun2(1,2,3,a=8,b=9) #(1, 2, 3) {'a': 8, 'b': 9}


