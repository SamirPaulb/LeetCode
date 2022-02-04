class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://leetcode.com/discuss/86025/java-clean-o-n-solution-with-explanation
        ls = len(nums)
        index = 0
        while index < ls:
            # nums[nums[index] - 1] == nums[index] means that the num is in right position
            if nums[index] <= 0 or nums[index] > ls or nums[nums[index] - 1] == nums[index]:
                index += 1
            else:
                # swap current num to correct position
                pos = nums[index] - 1
                nums[index], nums[pos] = nums[pos], nums[index]
        res = 0
        while res < ls and nums[res] == res + 1:
            res += 1
        return res + 1
