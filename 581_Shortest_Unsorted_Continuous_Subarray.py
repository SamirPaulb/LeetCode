class Solution(object):
    # https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/
    # def findUnsortedSubarray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     snums = nums[::]
    #     snums.sort()
    #     start = len(nums)
    #     end = 0
    #     for i in range(len(nums)):
    #         if snums[i] != nums[i]:
    #             start = min(start, i)
    #             end = max(end, i)
    #     if end >= start:
    #         return end - start + 1
    #     return 0

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        l, r = len(nums), 0
        for i in range(len(nums)):
            while len(stack) != 0 and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while len(stack) != 0 and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)
        if r > l:
            return r - l + 1
        return 0

    # def findUnsortedSubarray(self, nums):
    #     smin = 2 ** 31 -1
    #     smax = -2 ** 31
    #     flag = False
    #     for i in range(1, len(nums)):
    #         if nums[i] < nums[i-1]:
    #             flag = True
    #         if flag:
    #             smin = min(smin, nums[i])
    #     flag = False
    #     for i in range(len(nums)-2, -1, -1):
    #         if nums[i] > nums[i+1]:
    #             flag = True
    #         if flag:
    #             smax = max(smax, nums[i])
    #     for l in range(len(nums)):
    #         if smin < nums[l]:
    #             break
    #     for r in range(len(nums)-1, -1, -1):
    #         if smax > nums[r]:
    #             break
    #     if r > l:
    #         return r - l + 1
    #     return 0
