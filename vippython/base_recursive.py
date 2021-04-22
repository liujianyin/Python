'''计算阶层'''

def recursive1(a):
    if a==1:
        return 1
    else:
       return a*recursive1(a-1)

print(recursive1(3))

def Fibonacci(b):
    if b==1 or b==2:
        return 1
    else:
        return Fibonacci(b-1)+Fibonacci(b-2)

print(Fibonacci(6))


