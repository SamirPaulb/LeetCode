class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        for i in range(k):
            minElement = heapq.heappop(nums)
            heapq.heappush(nums, - minElement)
        
        return sum(nums)
            