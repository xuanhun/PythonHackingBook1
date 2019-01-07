# -*- coding: UTF-8 -*-
 
x=int(input('请输入一个整数:'))
if x==0:
    print('%d ==0' %x)
elif x<0:
    print('%d <0' %x)
else:
    print('%d >0' %x)

#for 
print('for 测试.....')
words = ['cat', 'window', 'defenestrate']
for word in words:
    print(word,len(word))

#利用切片复制列表
print('利用切片复制列表.....')
for word in words[:]:
    if len(word)>6:
        words.insert(0,word)
print(words)

#while
print('while.....')
count=0
while(count<9):
    print('the index is:',count)
    count +=1

#range
print('range.....')
a=range(5)
b=range(2,5)
c=range(2,5,2)
 
print(a)
print(b)
for i in c:
    print("value is",i)

#break
print('break.....')
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

#continue
print('continue.....')
for num in range(2,10):
    if(num %2 ==0):
        continue
    print(num)

#pass
def funcname(parameter_list):
    pass
 
class classname(object):
    pass
 
if a==0:
    pass
else:
    pass