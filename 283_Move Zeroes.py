class Solution(object):
    # def moveZeroes(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     # O(n^2)
    #     ls = len(nums)
    #     pos = 0
    #     while pos < ls:
    #         if nums[pos] == 0:
    #             curr = pos + 1
    #             while curr < ls:
    #                 if nums[curr] != 0:
    #                     temp = nums[curr]
    #                     nums[curr] = nums[pos]
    #                     nums[pos] = temp
    #                     break
    #                 curr += 1
    #         pos += 1

    def moveZeroes(self, nums):
        # O(n)
        ls = len(nums)
        n_pos = 0
        for i in range(ls):
            if nums[i] != 0:
                temp = nums[n_pos]
                nums[n_pos] = nums[i]
                nums[i] = temp
                n_pos += 1


