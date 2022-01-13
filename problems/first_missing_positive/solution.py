# https://youtu.be/-lfHWWMmXXM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            correctPos = nums[i] - 1
            
            while 0 <= correctPos < n and nums[correctPos] != nums[i]:
                nums[i], nums[correctPos] = nums[correctPos], nums[i]
                correctPos = nums[i] - 1
            
        for i in range(n):
            if i+1 != nums[i]: return  i+1
        
        return n+1