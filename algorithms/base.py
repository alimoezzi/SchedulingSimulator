from queue import Queue

from worker import Worker
from time import sleep


class BaseSch:
    def __init__(self, burstArray: list, priorityArray: list) -> None:
        self.burstArray = burstArray
        self.waitArray = [0 for i in burstArray]
        self.comArray = [0 for i in burstArray]
        self.processArray = [Worker(process) for i in range(len(burstArray))]
        self.q = Queue()

    def pickNext(self):
        pass

    def run(self):
        pass


def process(t, i, b):
    while b[i] > 0:
        b[i] -= 1
        sleep(0.001)
