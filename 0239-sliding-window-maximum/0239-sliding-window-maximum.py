### Solution 1 # Using Queue
class Solution:
    def maxSlidingWindow(self, nums, k):
        q = collections.deque()
        res = []
        
        for i, ch in enumerate(nums):
            while q and nums[q[-1]] <= ch:
                q.pop()
            if q and i - q[0] >= k:
                q.popleft()
            q.append(i)
            if i >= k-1: res.append(nums[q[0]])
        
        return res
    
    
### Solution 2 # Using MaxHeap
import heapq
class Solution:
    def maxSlidingWindow(self, nums, k):
        maxHeap = []
        res = []
        l = r = 0
        for r, ch in enumerate(nums):
            heapq.heappush(maxHeap, (-ch, r))
            if r-l+1 > k: l += 1
            while maxHeap and maxHeap[0][1] < l:
                heapq.heappop(maxHeap)
            if r >= k-1 and maxHeap:
                res.append(-maxHeap[0][0])
        
        return res