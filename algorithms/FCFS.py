from queue import Queue
from algorithms import BaseSch
from worker import Worker
from time import sleep


class FCFS(BaseSch):
    def pick_next(self):
        if self.i is None and self.w is None:
            w, i = self.q.popleft()
            return w, i
        elif self.burstArray[self.i] > 0:
            return self.w, self.i
        else:
            w, i = self.q.popleft()
            return w, i

    def init_queue(self):
        a = [(self.arrivalArray[i], i) for i in range(len(self.arrivalArray))]
        a.sort(key=lambda x: x[0])
        for i in range(len(self.burstArray)):
            self.q.append(self.processArray[a[i][1]])


if __name__ == '__main__':
    f = FCFS([0, 2, 4, 6, 8], [3, 6, 4, 5, 2])
    f.run()
    print('wait',f.waitArray)
    print('com',f.comArray)
    print('burst',f.burstArray)
    print('raw',f.raw)
