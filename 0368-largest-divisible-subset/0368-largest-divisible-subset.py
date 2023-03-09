class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[nums[i]] for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        
        res = []
        for i in range(len(nums)):
            if len(dp[i]) > len(res):
                res = dp[i]
        
        return res