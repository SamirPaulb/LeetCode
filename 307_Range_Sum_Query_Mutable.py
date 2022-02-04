# import math
#
# class NumArray(object):
#     def __init__(self, nums):
#         """
#         initialize your data structure here.
#         :type nums: List[int]
#         """
#         self.nums = list(nums)
#         ls = len(nums)
#         self.ls = int(math.ceil(math.sqrt(ls)))
#         self.b = [0] * self.ls
#         for i in range(ls):
#             self.b[i / self.ls] += nums[i]
#
#     def update(self, i, val):
#         """
#         :type i: int
#         :type val: int
#         :rtype: int
#         """
#         b_l = i / self.ls
#         self.b[b_l] = self.b[b_l] - self.nums[i] + val
#         self.nums[i] = val
#
#     def sumRange(self, i, j):
#         """
#         sum of elements nums[i..j], inclusive.
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         res = 0
#         startBlock = i / self.ls
#         endBlock = j / self.ls
#         if startBlock == endBlock:
#             res = sum(self.nums[i:j + 1])
#         else:
#             res += sum(self.nums[i:(startBlock + 1) * self.ls])
#             res += sum(self.b[startBlock + 1: endBlock])
#             res += sum(self.nums[endBlock * self.ls:j + 1])
#         return res


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.ls = len(nums)
        self.tree = [0] * (self.ls * 2)
        self.buildTree(nums)

    def buildTree(self, nums):
        i, j = self.ls, 0
        while i < 2 * self.ls:
            self.tree[i] = nums[j]
            i += 1
            j += 1
        for i in reversed(range(1, self.ls)):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2  + 1]


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        i += self.ls
        self.tree[i] = val
        while i > 0:
            left = right = i
            if i % 2 == 0:
                right = i + 1
            else:
                left = i -1
            self.tree[i / 2] = self.tree[left] + self.tree[right]
            i /= 2

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        i += self.ls
        j += self.ls

        while i <= j:
            if i % 2 == 1:
                res += self.tree[i]
                i += 1
            if j % 2 == 0:
                res += self.tree[j]
                j -= 1
            i /= 2
            j /= 2
        return res


        # Your NumArray object will be instantiated and called as such:
        # numArray = NumArray(nums)
        # numArray.sumRange(0, 1)
        # numArray.update(1, 10)
        # numArray.sumRange(1, 2)