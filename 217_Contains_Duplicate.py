class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # use set to check duplicate
        return len(nums) != len(set(nums))

    # def containsDuplicate(self, nums):
    #     nums.sort()
    #     for i in range(len(nums) - 1):
    #         if nums[i] == nums[i + 1]:
    #             return True
    #     return False