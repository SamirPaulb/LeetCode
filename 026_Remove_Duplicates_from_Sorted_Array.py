class Solution(object):
    # def removeDuplicates(self, nums):
    #     """
    #         :type nums: List[int]
    #         :rtype: int
    #         """
    #     ls = len(nums)
    #     if ls <= 1:
    #         return ls
    #     last = nums[0]
    #     pos = 1
    #     for t in nums[1:]:
    #         if t == last:
    #             continue
    #         else:
    #             nums[pos] = t
    #             pos += 1
    #             last = t
    #     return pos

    # https://leetcode.com/articles/remove-duplicates-sorted-array/
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        left = 0
        for i in range(1, len(nums)):
            if nums[left] == nums[i]:
                continue
            else:
                left += 1
                nums[left] = nums[i]
        return left + 1

