# -*- coding: UTF-8 -*-

import threading
import time
class MyThread(threading.Thread):
        def __init__(self,id):
                super(MyThread, self).__init__()
                self.id = id
        def run(self):
                time.sleep(3)
                print(self.id)
 
if __name__ == "__main__":
        t1=MyThread(999)
        t1.start()
        t1.join()
        for i in range(5):
            print(i)

