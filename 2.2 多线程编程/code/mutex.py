# -*- coding: UTF-8 -*-

import threading
import time

num = 0
def run(n):
    lock.acquire()  #获取锁
    global num
    print('start:', num)
    num += 1
    print('end', num)
    lock.release()  #释放锁

lock = threading.Lock()  # 实例化一个锁对象
for i in range(200):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()
    t.join()
