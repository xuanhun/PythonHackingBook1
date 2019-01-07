# -*- coding: UTF-8 -*-
def sayhi():
    print('Hi, this is newmodule speaking.')


version = '0.1'


class Singleton(object):

    __instance = None

    def __new__(cls, *args, **kw):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


class Person(Singleton):

    def __init__(self, name):
        self.name = name


# p1 = Person('xuanhun')
# print(p1.name)
# p2 = Person('sllsl')
# print(p2.name)
# print(p1.name)


class CC:
    name = 'cc'
