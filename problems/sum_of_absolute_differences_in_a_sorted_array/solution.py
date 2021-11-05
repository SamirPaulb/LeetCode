class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_left = 0
        sum_total = sum(nums)
        res = []
        
        for i in range(n):
            res.append((i * nums[i] - sum_left) + (sum_total - sum_left - (n - i) * nums[i]))
            sum_left += nums[i]
        
        return res
    
            
        