# -*- coding: UTF-8 -*-
 
import sys
 
print('The command line arguments are:')
for i in sys.argv:
    print(i)
 
print('\n\nThe PYTHONPATH is', sys.path, '\n')

 
if __name__ == '__main__':
    print('当前代码被单独运行')
else:
    print('当前代码被导入运行')

import myModule
 
myModule.sayhi()
print('Version', myModule.version)

print(dir(sys))
a=5
print(dir())
del a
print(dir())