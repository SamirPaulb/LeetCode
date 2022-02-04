class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # greedy
        # https://leetcode.com/articles/jump-game/
        length = len(nums)
        begin = length - 1
        for i in reversed(range(length - 1)):
            if i + nums[i] >= begin:
                begin = i
        return not begin