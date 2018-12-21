# -*- coding:utf-8 -*-


a=[1,2,3,4,5,6,7,8,9]

#使用reversed()
#注意：reversed()函数返回的是一个迭代器，而不是一个List，
# 需要再使用List函数转换一下。
b=list(reversed(a))
print(b)

#使用分片
#其中[::-1]代表从后向前取值，每次步进值为1
c=a[::-1]
print(c)

