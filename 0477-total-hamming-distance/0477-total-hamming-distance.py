class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            zero, one = 0, 0
            for num in nums:
                if num & (1<<i):
                    one += 1
                else: 
                    zero += 1
            res += zero * one
        
        return res