# -*- coding: UTF-8 -*-

from multiprocessing import Process, Queue
import time

def f(q, data):
    q.put(data)
def out(q):
    time.sleep(4)
    print(q.get())

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q, [1, 2, 3]))
    p.start()
   
    p.join()

    p1 = Process(target=out,args=(q,))
    p1.start()
    
    p1.join()
  