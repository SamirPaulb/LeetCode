import heapq
class FreqStack:

    def __init__(self):
        self.cnt = collections.Counter()
        self.maxHeap = []
        self.i = 0

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        self.i += 1
        heapq.heappush(self.maxHeap, (-self.cnt[val], -self.i, val))
        
    def pop(self) -> int:
        val = self.maxHeap[0][2]
        self.cnt[val] -= 1
        heapq.heappop(self.maxHeap)
        return val
