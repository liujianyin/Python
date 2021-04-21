'''创建字典'''
dict1=dict(name='liujy',age=18)
dict2={'name':'liujy','age':18}
dict3={} #创建空字典
print(dict1['name'])
# print(dict1['ldk']) #KeyError: 'ldk' 如果查询不存在的是报错
print(dict2.get('name1'))
# print(dict1.get('kdsjk')) #None 使用get方式，查不存在是返回none
print(dict2.get('ihdsafjhf'),999)  #如果想返回默认值，语法是后面加默认输出的值

'''对字典key值判断可以用in not in'''
dict4={'a':1,'b':2}
print('c' in dict4) #false

'''del 根据键删除指定的键值对'''
del dict4['a'] #{'b': 2}
dict4.clear() #{} 清空字典元素
dict4['c']=3 #{'c': 3} 增加元素
dict4['c']=6 #{'c': 6} 修改元素

dict5=dict(a=123,b=234,c=345)
keys=dict5.keys()
print(keys) #dict_keys(['a', 'b', 'c'])
values=dict5.values()
print(values) #dict_values([123, 234, 345])
items=dict5.items()
print(items) #dict_items([('a', 123), ('b', 234), ('c', 345)])
print(list(keys))  #视图转换为列表['a', 'b', 'c']
print(list(values))
print(list(items)) #[('a', 123), ('b', 234), ('c', 345)]  列表里面的存储这元组格式就是（）


'''遍历字典元素'''
dict6={'city':'shanghai','area':'pudong','road':'haiqu'}
for item in dict6:
    print(item,dict6.get(item))
'''city shanghai
area pudong
road haiqu'''

'''字典生成式'''
key_list=['name','age']
value_list=['ljy',18]
dict7={key_list:value_list for key_list,value_list in zip(key_list,value_list)}
print(dict7) #{'name': 'ljy', 'age': 18}
dict8={key_list.upper():value_list for key_list,value_list in zip(key_list,value_list)}
print(dict8) #{'NAME': 'ljy', 'AGE': 18}

