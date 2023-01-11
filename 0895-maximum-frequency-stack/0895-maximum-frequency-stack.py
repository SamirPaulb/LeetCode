import heapq
class FreqStack:

    def __init__(self):
        self.cnt = collections.Counter()
        self.maxHeap = []
        self.indx = 0

    def push(self, val):
        self.cnt[val] += 1
        self.indx += 1
        heapq.heappush(self.maxHeap, (-self.cnt[val], -self.indx, val))
        
    def pop(self):
        val = self.maxHeap[0][2]
        self.cnt[val] -= 1
        heapq.heappop(self.maxHeap)
        return val
