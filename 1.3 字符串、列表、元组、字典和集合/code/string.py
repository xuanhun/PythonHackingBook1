# -*- coding:utf-8 -*-

#声明字符串
str1 ='Hello World!'
str2 ="hello 玄魂！"
print('声明字符串.....')
print(str1)
print(str2)

#访问字符内容
print('访问字符内容.....')
print("str1[0]: ", str1[0])
print("str2[1:5]: ", str2[1:5])

#字符串操作符
print('字符串操作符.....')
a ="Hello"
b ="Python"
 
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a *2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
 
if("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")
 
if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")
 
print (r'\n')
print (R'\n')

#格式化
print('字符串格式化.....')
print("My name is %s and weight is %d kg!"%('玄魂',71))

print("formart method call:My name is {name} and weight is {weight} kg!".format(name="玄魂",weight=71))

#三引号
print('三引号.....')
hi = '''hi
  i am  玄魂'''
print(hi)

