class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        for i in range(len(nums)):
            tmp = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    tmp = max(tmp, dp[j])
            dp[i] = tmp+1
        
        return max(dp)