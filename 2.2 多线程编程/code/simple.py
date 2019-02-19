# -*- coding: UTF-8 -*-
import threading

class SimpleCreator():
    def f(self,id):
        print('线程执行 %s \n' %id)
        return
    def __init__(self):
        return
        
    def creatThread(self):
        for i in range(3):
            t = threading.Thread(target=self.f,args=(i,))
            t.start()
    


if __name__ == '__main__':
    sc = SimpleCreator()
    sc.creatThread()
