from collections import deque
from copy import deepcopy
from math import floor, ceil

from worker import Worker, create_worker
from worker import sleep as wsleep
from time import sleep


class BaseSch:
    start = False

    def __init__(self, arrivalArray: list, burstArray: list, priorityArray: list = None) -> None:
        self.arrivalArray = arrivalArray
        self.priorityArray = priorityArray
        self.burstArray = burstArray
        self.waitArray = [0 for i in burstArray]
        self.comArray = deepcopy(burstArray)
        self.processArray = [(Worker(self.process), i) for i in range(len(burstArray))]
        self.q = deque()
        self.w = None
        self.i = None
        self.init_queue()
        self.elapse_time = 0
        for i in range(len(self.burstArray)):
            self.processArray[i][0].stop()

    def init_queue(self):
        pass

    def pick_next(self) -> (Worker, int):
        pass

    def run(self):
        for i in range(len(self.burstArray)):
            self.processArray[i][0].stop()
        print('run')
        while sum(self.burstArray) != 0:
            w, i = self.pick_next()
            BaseSch.start = True
            if self.w is None and self.i is None:
                self.w, self.i = w, i
                self.w.start(index=self.i)
                self.end(i)
            elif i != self.i:
                self.w.stop()
                self.w, self.i = w, i
                sleep(0.001)
                self.w.start(index=self.i)
                self.end(i)
            else:
                self.w.stop()
                sleep(0.001)
                self.w.start(index=self.i)
                self.end(i)
            self.elapse_time += 1
            self.addAll(self.i, self.elapse_time)

    def end(self, i):
        if self.burstArray[i] == 0:
            print('stopping thread', i, 'remaining', sum(self.burstArray))
            self.w.stop()

    def addAll(self, i, t):
        for j in range(len(self.waitArray)):
            if j != i:
                if self.burstArray[j] > 0:
                    if self.elapse_time > self.arrivalArray[j]:
                        self.waitArray[j] += 1

    def process(self, index=None):
        while self.burstArray[index] > 0:
            if BaseSch.start:
                print('\nthread' + str(index) + str(self.burstArray[index]) + '\n')
                self.burstArray[index] -= 1
                wsleep(0.001)
