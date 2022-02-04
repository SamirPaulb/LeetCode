class Solution(object):
    # def wiggleSort(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     # Sort
    #     if nums is None or len(nums) == 0:
    #         return
    #     nums.sort()
    #     # n - x - 1 = x
    #     wiggle = (len(nums) - 1) / 2
    #     for i in range(wiggle):
    #         pos = i * 2 + 1
    #         nums.insert(pos, nums.pop(-1))

    # def wiggleSort(self, nums):
    #     if nums is None or len(nums) == 0:
    #         return
    #     nums.sort()
    #     for i in range(1, len(nums) - 1, 2):
    #         # swap i and i + 1
    #         nums[i], nums[i + 1] = nums[i + 1], nums[i]

    # def wiggleSort(self, nums):
    #     less = True
    #     for i in range(len(nums) - 1):
    #         if less:
    #             if nums[i] > nums[i + 1]:
    #                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
    #         else:
    #             if nums[i] < nums[i + 1]:
    #                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
    #         less = not less

    def wiggleSort(self, nums):
        for i in range(len(nums) - 1):
            if (i % 2 == 0 and nums[i] > nums[i + 1]) or\
               (i % 2 == 1 and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
