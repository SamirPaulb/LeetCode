class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        res = 0
        while i < len(nums):
            tmp = 0
            while i < len(nums) and nums[i] == 1:
                tmp += 1
                i += 1
            res = max(res, tmp)
            i += 1
        return res