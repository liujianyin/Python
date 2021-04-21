'''字符串神奇现象'''
str1='sdavfdsf'
str2='sdavfdsf'
print(id(str1)==id(str2)) #true

str3='ghs%'
str4='ghs%'
print(id(str3)==id(str4))
#true  不满足标识符，因为含有%   因为编辑器进行了优化，如果在交互式的话会是false
#字符串的驻留机制 jion连接 比 + 效率高很多


'''字符串查询操作'''
str5='helloljy'
print(str5.index('l')) #2 如果找不存在的会报错
print(str5.find('l')) #从前往后第一次出现 2 如果找不存在的会返回-1
print(str5.rindex('l')) #5
print(str5.rfind('l')) #从后往前第一次出现 5

'''字符串的大小写转换'''

str6='heLLo World'
print(str6.upper()) #全转换大写
print(str6) #skhfdjewhgrj
print(str6.lower())#全转换小写
print(str6.swapcase())#大->小 小->大
print(str6.capitalize())#第一字符大写 其余小写
print(str6.title())#第一词的第一个字符大写 其余小写

'''字符串对齐操作'''
str7='hsgfjwfg'
print(str7.center(20,'*'))  #20个字符空间中间对齐，空格填*   ******hsgfjwfg******
print(str7.ljust(20,'*'))  #20个字符空间左对齐，空格填*      hsgfjwfg************
print(str7.rjust(20,'*'))  #20个字符空间左右对齐，空格填*    ************hsgfjwfg
print(str7.zfill(20)) #右对齐 填充0，只有一个参数是字符个数   000000000000hsgfjwfg

'''字符串分割'''
str8='hk love liujy'
print(str8.split())  #['hk', 'love', 'liujy']
print(str8.split('l')) # ['hk ', 'ove ', 'iujy']
print(str8.split('l',1)) #['hk ', 'ove liujy']
print(str8.rsplit())  #['hk', 'love', 'liujy']
print(str8.rsplit('l')) # ['hk ', 'ove ', 'iujy']
print(str8.rsplit('l',1)) #['hk love ', 'iujy']  靠右分割

'''字符串常用函数'''
str9 = "this is string example....wow!!! this is really string"
print(str9.replace("is", "was")) #thwas was string example....wow!!! thwas was really string
print(str9.replace("is", "was", 2))  #最大替换次数不得超过2次 #thwas was string example....wow!!! this is really string


'''字符串切片'''
str10='hello liujy'
print(str10[1:4:1]) #ell

'''格式化字符串'''
name='liujy'
age=18
print('名字%s,年纪%d'%(name,age))
print('名字{0},年纪{1}'.format(name,age))
print(f'名字{name},年纪{age}')



