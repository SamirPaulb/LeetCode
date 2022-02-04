class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ls = len(nums)
        if ls <= 1:
            return
        pair = []
        for i in range(ls):
            for j in range(i + 1, ls):
                # append ascending order pair
                if nums[i] < nums[j]:
                    pair.append([i,j])
        pos = 0
        if len(pair) > 0:
            self.swap(nums, pair[-1][0], pair[-1][1])
            pos = pair[-1][0] + 1
        # sort from pos
        for i in range(pos, ls):
            for j in range(i + 1, ls):
                if nums[i] > nums[j]:
                    self.swap(nums, i, j)

    def swap(self, nums, index1, index2):
        if index1 == index2:
            return
        nums[index1], nums[index2] = nums[index2], nums[index1]

    # def nextPermutation(self, nums):
    #     # https://leetcode.com/discuss/86630/fast-and-easy-python-solution-beaten-79%25
    #     pos = -1
    #     ls = len(nums)
    #     for i in range(ls - 1, 0, -1):
    #         if nums[i] > nums[i - 1]:
    #             pos = i - 1
    #             break
    #     if pos == -1:
    #         self.re_order(nums, 0, ls - 1)
    #         return
    #     for i in range(ls - 1, -1, -1):
    #         if nums[pos] < nums[i]:
    #             nums[pos], nums[i] = nums[i], nums[pos]
    #             self.re_order(nums, pos + 1, ls - 1)
    #             break
    #
    # def re_order(self, a, start, end):
    #     for i in range(0, (end - start + 1) // 2):
    #         a[start + i], a[end - i] = a[end - i], a[start + i]




