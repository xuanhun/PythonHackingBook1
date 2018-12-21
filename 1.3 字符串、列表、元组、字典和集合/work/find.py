# -*- coding:utf-8 -*-

# 实现字符串查找和替换
# Python 查找字符串使用 变量.find("要查找的内容"[，开始位置，结束位置])，
# 开始位置和结束位置，表示要查找的范围，为空则表示查找所有。查找到后会返回位置，位置从0开始算，如果没找到则返回-1

str = 'a,hello，xuanhun,玄魂，xuanhun'
toFind = 'xuanhun'
str1 = str
index = 0
while(str1.find(toFind) > 0):
    index += str1.find(toFind)
    print('找到子串在位置:', index)
    index += 7
    str1 = str1[(index):]
# 字符串替换 使用replace方法

replace = 'cccc'
str2 = str.replace('xuanhun', replace)
print('替换后', str2)
