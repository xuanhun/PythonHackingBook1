# -*- coding: UTF-8 -*-


#Print('hello')


# while True:
#     try:
#         n = input("请输入一个整数: ")
#         n = int(n)
#         break
#     except ValueError as e:
#         print("无效数字，再次输入 ...",e)
# print("输入成功!")


# import sys

# try:
#     f = open('integers.txt')
#     s = f.readline()
#     i = int(s.strip())
# except IOError as e:
#     print("I/O error",e)
# except ValueError:
#     print("No valid integer in line.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise


# try:
#     f = open('integers.txt')
#     s = f.readline()
#     i = int(s.strip())
# except (IOError, ValueError):
#     print("An I/O error or a ValueError occurred")
# except:
#     print("An unexpected error occurred")
#     raise


# class ShortInputException(Exception):
#     '''A user-defined exception class.'''
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
 
# try:
#     s = input('Enter something --> ')
#     if len(s) < 3:
#         raise ShortInputException(len(s), 3)
#     # Other work can continue as usual here
# except EOFError:
#     print('\nWhy did you do an EOF on me?')
# except ShortInputException as x:
#     print('ShortInputException: The input was of length %d, \
#           was expecting at least %d' % (x.length, x.atleast))
# else:
#     print('No exception was raised.')


def test1():
   try:
      print('to do stuff')
      raise Exception('hehe')
   except Exception:
      print('process except')
      print('to return in except')
      return 'except'
   finally:
      print('to return in finally')
      return 'finally'
 
test1Return = test1()
print('test1Return : ' + test1Return)