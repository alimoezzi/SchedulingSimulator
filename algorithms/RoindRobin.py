from queue import Queue
from algorithms import BaseSch
from worker import Worker
from time import sleep


class RR(BaseSch):
    def pick_next(self):
        w, i = self.q.popleft()
        if self.burstArray[i] > 0:
            self.q.append((w, i))
        return w, i

    def init_queue(self):
        a = [(self.arrivalArray[i], i) for i in range(len(self.arrivalArray))]
        a.sort(key=lambda x: x[0])
        for i in range(len(self.burstArray)):
            self.q.append(self.processArray[a[i][1]])


if __name__ == '__main__':
    f = RR([0, 1, 2, 3, 3], [8, 1, 4, 6, 2])
    f.run()
    print('wait', f.waitArray)
    print('com', f.comArray)
    print('burst', f.burstArray)
