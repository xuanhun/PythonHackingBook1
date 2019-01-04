# -*- coding: UTF-8 -*-


import tempfile
import stat
import sys
import os

os.chdir('/Users/xuanhun/玄魂工作室/python黑客编程/python黑客编程入门版/2.1 文件和目录基本操作/code/sampleDirectory')


def listCurrentDirectory(path):
    files = os.listdir(path)
    for name in files:
        print(name)


def listDirectoryDetail(path):
    files = os.listdir(path)
    for name in files:
        pathName = os.path.join(path, name)
        print("%s文件或者目录信息：....." % pathName)
        print(os.stat(pathName).st_mode)  # 权限模式
        print(os.stat(pathName).st_ino)  # inode number
        print(os.stat(pathName).st_dev)  # device
        print(os.stat(pathName).st_nlink)  # number of hard links
        print(os.stat(pathName).st_uid)  # 所有用户的user id
        print(os.stat(pathName).st_gid)  # 所有用户的group id
        print(os.stat(pathName).st_size)  # 文件的大小，以位为单位
        print(os.stat(pathName).st_atime)  # 文件最后访问时间
        print(os.stat(pathName).st_mtime)  # 文件最后修改时间
        print(os.stat(pathName).st_ctime)  # 文件创建时间


def listCurrentDirectoryMode(path):
    files = os.listdir(path)
    for name in files:
        pathName = os.path.join(path, name)
        mode = os.stat(pathName).st_mode
        if stat.S_ISDIR(mode):
            # 如果是文件夹
            print('%s是文件夹' % pathName)
        elif stat.S_ISREG(mode):
            # 如果是文件
            print('%s是文件' % pathName)
        else:
            # 未知类型
            print('未知目录类型 %s' % pathName)

# listCurrentDirectoryMode('.')


def printChmode(path):
    files = os.listdir(path)
    for name in files:
        pathName = os.path.join(path, name)
        mode = os.stat(pathName).st_mode
        print(stat.filemode(mode))

# printChmode('.')


def walkDir(path):
    for dirName, subdirList, fileList in os.walk(path):
        print('发现目录: %s' % dirName)
        for fname in fileList:
            print('\t%s' % fname)

# walkDir('.')


def renameTest():
    walkDir('.')
    os.rename('1.txt', '2.txt')
    try:
        os.rename('./a/a.p', './b2/b.p')
    except FileNotFoundError as e:
        print(e)
    os.renames('./a/a1/a1.t', 'b/b2/b1.t')
    walkDir('.')

# renameTest()


def createPath(p):
    try:
        os.makedirs(p)
    except OSError as e:
        print('创建目录失败', e)
    else:
        print('目录%s创建成功' % p)

# createPath('./a/')


def createPath2(p):
    try:
        if not os.path.exists(p):
            os.makedirs(p)
            print('%s创建成功' % p)
        else:
            print('%s已经存在' % p)
    except OSError as e:
        print('创建目录失败', e)


# createPath2('./a/')
# createPath2('./a/b')

def createPath3(p, mode):
    try:
        if not os.path.exists(p):
            os.makedirs(p, mode,)
            print('%s创建成功' % p)
            mode = os.stat(p).st_mode
            print(stat.filemode(mode))
        else:
            print('%s已经存在' % p)
    except OSError as e:
        print('创建目录失败', e)

# createPath3('./a/b/c',0o755)


def createTempDirectory():
    with tempfile.TemporaryDirectory() as directory:
        print('临时目录 %s' % directory)


createTempDirectory()


def removeDir(path):
    try:
        os.rmdir(path)
    except OSError:
        print("删除 %s 失败" % path)
    else:
        print("删除 %s成功" % path)
