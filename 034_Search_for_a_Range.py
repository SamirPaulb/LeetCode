class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length == 0:
            return [-1, -1]
        min = 0
        max = length - 1
        while min <= max:
            pos = (min + max) / 2
            if nums[pos] > target:
                max = pos - 1
            elif nums[pos] < target:
                min = pos + 1
            else:
                # when nums[pos] == target
                # find the min and max
                for i in range(min, max + 1):
                    if nums[i] == target:
                        if min < i and nums[min] != nums[i]:
                            min = i
                        max = i
                return [min, max]
        return [-1, -1]