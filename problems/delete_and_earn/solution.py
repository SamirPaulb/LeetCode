class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        a = [0]*(max(nums)+1)
        for i in nums:
            a[i] += i
        dp = [0]*len(a)
        
        for i in range(len(a)):
            if i == 0:
                dp[i] = a[i]
            elif i == 1:
                dp[i] = max(a[i-1], a[i])
            else:
                dp[i] = max(a[i]+dp[i-2], dp[i-1])
        return dp[-1]
        
        