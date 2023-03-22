class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        dp = [0] * n
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        
        return sum(dp)
    
# Time: O(n)
# Space: O(n)
    
    

class Solution:
    def numberOfArithmeticSlices(self, nums):
        dp = 0; n = len(nums); res = 0
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp += 1
                res += dp
            else:
                dp = 0
                
        return res
    
# Time: O(n)
# Space: O(1)