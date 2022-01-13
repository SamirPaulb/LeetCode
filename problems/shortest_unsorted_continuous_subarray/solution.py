# https://www.youtube.com/watch?v=hi9Z7EdsEfw

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minV = float("inf")
        maxV = float("-inf")
        n = len(nums)
        
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                minV = min(minV, nums[i])
        
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                maxV = max(maxV, nums[i])
        
        if minV == float("inf") and maxV == float("-inf"): return 0
        
        start = 0; end = n-1
        
        while start < n:
            if nums[start] > minV:
                break
            start += 1
        
        while end >= 0:
            if nums[end] < maxV:
                break
            end -= 1
        
        return end - start + 1