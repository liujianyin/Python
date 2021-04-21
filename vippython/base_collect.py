'''集合的创建'''
collect1={1,2,3,4,1,2,3,4} #集合中元素不能重复、和字典中的key值不能重复
print(collect1) #{1, 2, 3, 4} 输出结果直接去重,集合中的元素是无序的
collect2=set({1,2,3,4}) #将集合转换为集合
collect3=set(range(6))
collect4=set([1,2,3,4])#将列表转换为集合
collect5=set((1,2,3,4))#将元组转换为集合
collect6=set('hello') #字符串转换为集合
set() #定义空集合

'''集合的相关操作'''
collect7={1,2,3,4,5}
print(10 in collect7)
print(2 in collect7)
collect7.add(12) #只能添加一个元素
print(collect7)
collect7.update({12,143,1323,5}) #只能添加一个元素或者多个元素
collect7.update([12,143,1323,5]) #列表
collect7.update((12,143,1323,67)) #元组
print(collect7)
collect7.remove(1) #移除元素 如果删除的元素不存在会抛异常
print(collect7)
collect7.discard(1) #丢弃元素，如果丢了不存在的不会抛异常
collect7.pop() #随机删除一个元素
collect7.clear()#清空元素
print(collect7) #set()结果是空元素

'''集合之间的关系'''
collect8={1,3,5,7}
collect9={3,7,5,1}
print(collect8==collect9)#true 集合是无序的所以相等
collect10={1,2}
collect11={1,2,4,5}
collect12={1,2,4,56}
print(collect10.issubset(collect12)) #true collect10是collect12的子集
print(collect11.issubset(collect10))#fasle collect11不是collect10的子集
print(collect10.issuperset(collect12)) #fasle collect10不是collect12的超集（父集的意思）
print(collect11.issuperset(collect10))#true collect11是collect10的超集（collect11包含collect10的意思）
print(collect11.isdisjoint(collect12))# false 表示是否没有关系
print(collect11.isdisjoint(collect10))# false 表示有交集


s1 = {2,3,1}
s2 = {2,3,4}
print('交集:',s1.intersection(s2))
print('交集:',s1 & s2)

# 差集
s1 = {2,3,1}
s2 = {2,3,4}
##  s1和s2的差集 s1中有哪些s2中没有的元素
print('差集:',s1.difference(s2))
print('差集:',s1 -s2)

# 对等差分:并集- 交集
s1 = {2,3,1}
s2 = {2,3,4}
print('对等差分:',s1.symmetric_difference(s2))
print('对等差分:',s1 ^ s2)

s3 = {'westos','redhat','python'}
s4 = {'redhat','westos','linux'}
# s3是否是s4的子集
print(s3.issubset(s4))
# 两个集合是不是不相交
print(s3.isdisjoint(s4))



'''集合生成式'''
collect13={item for item in range(16)}
print(collect13)