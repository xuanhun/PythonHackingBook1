# -*- coding: UTF-8 -*-
import os

print(os.getcwd())
filePath = './python黑客编程/python黑客编程入门版/2.1 文件和目录/code/test.txt'

file = open(filePath,'r')
print(file.read())
file.close()

print('读取部分内容.....')

file = open(filePath,'r')
print(file.read(3))
file.close()

print('二进制模式.....')

file = open(filePath,'rb')
print(file.read())
file.close()

print('逐行读取.....')
file = open(filePath,'r')
for c in file:
    print(c)
file.close()
print('分批读取.....')
with open(filePath,'r') as f:
  while True:
    c = f.read(1)
    if not c:
      break
    print(c)

print('a模式写入.....')

def printContent(path):
     with open(path,'r') as f:
         print(f.read())

with open(filePath,'a') as f:
    f.write("追加内容\r\n")
    
printContent(filePath)

# print('w模式写入.....')
# with open(filePath,'w') as f:
#     f.write("追加内容\r\n")
# printContent(filePath)

print('a模式写入，文件开始位置添加内容.....')
with open(filePath,'a') as f:
    f.seek(0)
    f.write("追加内容\r\n")
printContent(filePath)

import os

def removeTest():
    os.remove('./test.txt')

def renameTxt():
    os.rename('./test.txt','./abc.txt')
