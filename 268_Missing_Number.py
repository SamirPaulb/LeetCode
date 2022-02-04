class Solution(object):
    # def missingNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     return (n ** 2 + n) / 2 - sum(nums)

    def missingNumber(self, nums):
        res = len(nums)
        for i, v in enumerate(nums):
            res ^= i
            res ^= v
        return res
    
    # def missingNumber(self, nums):
    #     nums.sort()
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = (left + right) / 2
    #         if nums[mid] <= mid:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return left
