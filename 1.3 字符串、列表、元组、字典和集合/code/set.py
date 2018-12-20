# -*- coding: UTF-8 -*-
 
s1=set('abcdde')
s2=set([1,2,3,4,5])
s3 = frozenset("xuanhun")
 
print(type(s1))
print(type(s3))
print(s2)

#输出集合内容
for item in s3:
    print(item)

#update
s2=set([1,2,3,4,5])
print("原始数据：",s2)
s2.add("j")  
print("添加数据后：",s2)
s2.remove(3)
print("删除数据后：",s2)
s2.update([6,7,8,9])
print("update数据后：",s2)

#union
s1=set('abcdde')
s2=set([1,2,3,4,5])
s4=s1|s2
print("s1|s2",s4)

#inter
print("s1&s2",s1&s2)

#dif
print("s1-s2",s1 -s2)
print("s1 dif  s2",s1.difference(s2))

