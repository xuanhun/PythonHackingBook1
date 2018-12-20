# -*- coding:utf-8 -*-
 
dict ={'Name':'Zara','Age':7,'Class':'First'}
 
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

#访问不存在的key
#print(dict['Xuanhun'])

#修改值

print("修改前",dict['Age'])
dict['Age']=8# update existing entry
print("修改后: ", dict['Age'])

#删除
del dict['Age']# 删除键是'Name'的条目
#print("dict['Age']: ", dict['Age'])#引发异常
dict.clear()    # 清空词典所有条目
print(dict)
del dict      # 删除词典
 
print(dict)    
