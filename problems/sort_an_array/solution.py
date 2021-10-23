import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        myHeap = []
        
        for i in nums:
            heapq.heappush(myHeap, i)
            
        ans = []
        
        for i in range(len(nums)):
            ans.append(heapq.heappop(myHeap))
            
        return ans