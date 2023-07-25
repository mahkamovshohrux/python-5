from threading import Thread

class MyThread(Thread):
    def __init__(self, n, m):
        Thread.__init__(self)
        self.n = n
        self.m = m

    def run(self):
        s = 1
        while self.m < 100:
            self.n, self.m = self.m, self.m + self.n
            s += self.n

        print(s)
obj = MyThread(1, 1)
obj.start()