'''列表的创建'''
lst1=list(['hello','liujy']);
lst2=['hello','hk']

'''list的索引获取'''
lst3=[1,2,3,4,5.1]
print(lst3.index(1))   #输出1,如果有多个查询字段，返回的是第一个的值的索引
print(lst3.index(3,1,3))  #从指定范围内（从index范围为1到3（不包含3）查询值为5）


'''list切片操作'''
lst4=[1,2,3,4,5,6,7,8,9,10]
print(lst4[2:9:2])  #[3, 5, 7, 9] 从index2到10 步长为2
print(lst4[9:0:-2]) #[10, 8, 6, 4, 2] 步长为负数代表反过来

'''list的crud'''
lst5=[1,2,3,4]
lst5.append(5)
print(lst5) #在list末尾添加一个元素  [1, 2, 3, 4, 5]   lst5的id没有变
lst6=['7',8]
lst5.append(lst6) #[1, 2, 3, 4, 5, ['7', 8]] 将lst6作为一个元素添加在末尾
lst5.extend(lst6) #[1, 2, 3, 4, 5, ['7', 8], '7', 8] 将lst6和lst5进行了融合（拓展）
lst5.insert(4,6) #[1, 2, 3, 4, 6, 5, ['7', 8], '7', 8]
lst5[2:]=lst6 #[1, 2, '7', 8]

lst7=[1,2,3,4,5,6,6,8,7,5]
lst7.remove(5) #[1, 2, 3, 4, 6, 6, 8, 7, 5] 传入的值是要移除的值，同时如果移除的有多个一样元素，则只移除第一个
lst7.pop(2)    #[1, 2, 4, 6, 6, 8, 7, 5] 删除传入的索引值的值，如果不传值则删除的是最后的一个值
lst7[2:4]=[] #[1, 2, 6, 8, 7, 5]
lst7.clear() #[]
del lst7  #删除整个列表元素


lst8=[1,2,3,4,5,6]
lst8[2]=10 #直接修改列表中的数组
lst8[2:3]=[5,5,5] # [1, 2, 5, 5, 5, 4, 5, 6] 切片修改值
print(lst8)

lst9=[34,12,4324,32,532,12,342,54,3243,2143]
lst9.sort(reverse=True) #[4324, 3243, 2143, 532, 342, 54, 34, 32, 12, 12]降序  不会产生新列表对象，对原列表进行排序
lst9.sort(reverse=False) #[12, 12, 32, 34, 54, 342, 532, 2143, 3243, 4324]升序，没有参数默认是升序 不会产生新列表对象，对原列表进行排序
print(lst9)
lst10=[34,12,4324,32,532,12,342,54,3243,2143]
lst11=sorted(lst10,reverse=True) # [4324, 3243, 2143, 532, 342, 54, 34, 32, 12, 12]
'''sorted()不会改变原来的list，而是会返回一个新的已经排序好的list
    list.sort()方法仅仅被list所定义，sorted()可用于任何一个可迭代对象'''


'''for 生成列表'''
lst12=[qw**2 for qw in range(1,10)]
print(lst12) #[1, 4, 9, 16, 25, 36, 49, 64, 81]


