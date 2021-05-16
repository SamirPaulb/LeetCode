class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        LL = []
        i = 0
        while i< len(nums):
            freq , val  = nums[i] , [nums[i+1] for j in range(nums[i])]
            LL +=val
            i += 2
        return LL
            
            
            