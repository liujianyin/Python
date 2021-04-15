'''创建字典'''
dict1=dict(name='liujy',age=18)
dict2={'name':'liujy','age':18}
dict3={} #创建空字典
print(dict1['name'])
# print(dict1['ldk']) #KeyError: 'ldk'
print(dict2.get('name'))
print(dict2.get['ldk'])