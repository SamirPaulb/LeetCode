class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        
        for i, ch in enumerate(nums):
            if q and i-q[0] >= k:
                q.popleft()
                
            while q and nums[q[-1]] < ch:
                q.pop()
            
            q.append(i)
            
            if i >= k-1:
                res.append(nums[q[0]])
        
        return res