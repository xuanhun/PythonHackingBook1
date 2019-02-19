# -*- coding: UTF-8 -*-
from threading import Thread


class MyThread(Thread):
    def __init__(self, id):
        super(MyThread, self).__init__()  # 重构run函数必须要写
        self.id = id

    def run(self):
        print("task", self.id)


if __name__ == "__main__":
    t1 = MyThread("t1")
    t2 = MyThread("t2")

    t1.start()
    t2.start()