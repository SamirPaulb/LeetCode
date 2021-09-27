class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        s = sum(nums)
        if s % 2 != 0: return False
        
        dp = [[False]*(s//2 + 1) for i in range(len(nums)+1)]
        
        for i in range(len(nums)+1):
            for j in range(s//2 + 1):
                if j == 0:
                    dp[i][j] = True
                elif nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        #print(dp)
        return dp[-1][-1]