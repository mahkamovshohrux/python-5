# HIGH CPU USAGE - 100% CPU USAGE
from threading import Thread

class MyThread(Thread):
    def __init__(self, n, m):
        Thread.__init__(self)
        self.n = n
        self.m = m

    def run(self):
        print(1)
        while self.m < 100:
            self.n, self.m = self.m, self.n + self.m
            print(self.n)
if __name__ == "__main__":
    obj = MyThread(1, 1)
    obj.start()
