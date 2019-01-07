# -*- coding: UTF-8 -*-

import myModule
import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')


if __name__ == '__main__':
    print('当前代码被单独运行')
else:
    print('当前代码被导入运行')
myModule.sayhi()
print('Version', myModule.version)
myModule.version = 0.5

import test

print(test.c1.name)


