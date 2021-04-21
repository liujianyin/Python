'''元组创建方式'''
tuple1=(1,2,3,4)
tuple2=tuple((1,2,3,4))
tuple3=1,2,3,4 #元组创建可以省略（）
tuple4=(10,)#如果元组里面只有1个元素，一定要使用（）并且，
tuple5=tuple()
tuple6=()  #空元组创建




tuple7=(1,2,3,[5,6],7)
tuple7[3].append(8) #输出元组中的值
print(tuple7)

tuple8=(1,2,3,4,5)
for item in tuple8:
    print(item) #可迭代对象，输出里面的值

