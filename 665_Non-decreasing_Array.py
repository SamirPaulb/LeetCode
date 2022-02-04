class Solution(object):
    # def checkPossibility(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     pos = None
    #     # Check if there are more than 2 broken point
    #     # record first index
    #     for i in range(len(nums) - 1):
    #         if nums[i] > nums[i + 1]:
    #             if pos is not None:
    #                 return False
    #             pos = i
    #     if pos is None or pos == 0 or pos == len(nums) - 2:
    #         return True
    #     # Remove pos or remove pos + 1
    #     return (nums[pos - 1] <= nums[pos + 1] or nums[pos] <= nums[pos + 2])

    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # https://leetcode.com/problems/non-decreasing-array/discuss/106826/JavaC%2B%2B-Simple-greedy-like-solution-with-explanation
        broken_num = 0
        for i in range(len(nums) - 1):
            if (nums[i] > nums[i + 1]):
                broken_num += 1
                if broken_num >= 2:
                    return False
                if (i - 1 < 0 or nums[i - 1] <= nums[i + 1]):
                    # Remove i
                    nums[i] = nums[i + 1]
                else:
                    # Remove i + 1
                    nums[i + 1] = nums[i]
        return True
