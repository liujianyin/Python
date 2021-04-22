try:
    a=int(input('输入数据a'))
    b=int(input('输入数据b'))
    c=a/b
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('输入格式不对')
except BaseException as e:
    print('出错了',e)
else:
    print('a/b的值是：',int(c))
finally:
    print('不管出什么错误,都需要跑这段')
