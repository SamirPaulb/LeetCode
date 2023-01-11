# https://leetcode.com/problems/maximum-frequency-stack/
# https://youtu.be/Z6idIicFDOE

'''
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
        
# Time: O(log(N))
# Space: O(N)
'''

class FreqStack:

    def __init__(self):
        self.cnt = collections.Counter()
        self.stackDict = {}
        self.maxcnt = 0

    def push(self, val):
        self.cnt[val] += 1
        if self.maxcnt < self.cnt[val]:
            self.maxcnt = self.cnt[val]
            self.stackDict[self.maxcnt] = [val]
        else:
            self.stackDict[self.cnt[val]].append(val)

    def pop(self):
        # print(self.stackDict)
        if not self.stackDict[self.maxcnt]:
            del self.stackDict[self.maxcnt]
            self.maxcnt -= 1
        val = self.stackDict[self.maxcnt].pop()
        self.cnt[val] -= 1
        return val