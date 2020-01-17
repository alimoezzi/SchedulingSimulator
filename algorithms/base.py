from queue import Queue

from worker import Worker
from time import sleep


class BaseSch:
    def __init__(self, burstArray: list, priorityArray: list) -> None:
        self.burstArray = burstArray
        self.waitArray = [0 for i in burstArray]
        self.comArray = burstArray
        self.processArray = [Worker(process) for i in range(len(burstArray))]
        self.q = Queue()
        self.w = None
        self.i = None

    def pickNext(self) -> (Worker, int):
        pass

    def run(self):
        while self.pickNext()[1] > 0:
            (w, i) = self.pickNext()
            if w != self.w:
                self.w.pause()
                self.w = Worker.start(i, self.burstArray)
                self.i = i
            sleep(0.001)
            self.w.pause()
            self.addAll(self.i)

    def addAll(self, i):
        for j in range(len(self.waitArray)):
            if (j != i):
                self.waitArray[j] += 1


def process(t, i, b):
    while b[i] > 0:
        b[i] -= 1
        sleep(0.001)
