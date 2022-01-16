class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minV = float("inf")
        maxV = float("-inf")
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                minV = min(minV, nums[i])
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                maxV = max(maxV, nums[i])
        
        if minV == float("inf") and maxV == float("-inf"): return 0
        
        start = 0; end = len(nums) - 1
        
        while start < len(nums):
            if nums[start] > minV:
                break
            start += 1
        
        while end >= 0:
            if nums[end] < maxV:
                break
            end -= 1
        
        print(end, start)
        return end - start + 1