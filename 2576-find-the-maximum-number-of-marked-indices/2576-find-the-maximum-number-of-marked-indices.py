class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        res = 0
        for r in range(n-n//2, n):
            if 2*nums[l] <= nums[r]:
                l += 1
                res += 2
        
        return res