from queue import Queue
from algorithms import BaseSch
from worker import Worker
from time import sleep


class SRT(BaseSch):
    def pick_next(self):
        return self.processArray[
            sorted(
                list(
                    filter(lambda x:self.elapse_time >= self.arrivalArray[x[0]],
                           list(filter(lambda x:x[1] > 0, enumerate(self.burstArray)))
                           )
                ),key=lambda x: x[1]
            )[0][0]
        ]
        # a = []
        # for i, j in enumerate(self.burstArray):
        #     if j != 0:
        #         if self.elapse_time >= self.arrivalArray[i]:
        #             a.append((i, j))
        # a.sort(key=lambda x: x[1])
        # print(str(self.w) + str(a[0][0]) + str(self.elapse_time) + str(a) + str(self.burstArray))
        # return self.processArray[a[0][0]]

    def init_queue(self):
        a = [(self.arrivalArray[i], i) for i in range(len(self.arrivalArray))]
        a.sort(key=lambda x: x[0])
        for i in range(len(self.burstArray)):
            self.q.append(self.processArray[a[i][1]])


if __name__ == '__main__':
    f = SRT([0, 0, 4, 6, 8], [3, 6, 4, 5, 2])
    f.run()
    print('wait', f.waitArray)
    print('com', f.comArray)
    print('burst', f.burstArray)
