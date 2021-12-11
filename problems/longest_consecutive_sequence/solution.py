import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        heapq.heapify(nums) # Now nums is a min heap
        
        sortedNums = []
        while nums:
            sortedNums.append(heapq.heappop(nums))
            
        prev = sortedNums[0]
        count  = 1
        res = 1
        for i in sortedNums[1:]:
            curr = i
            if curr - prev == 0: continue
            if curr - prev == 1:
                count += 1
                prev = curr
            else: 
                count = 1
                prev = curr
            res = max(res, count)
        
        return res