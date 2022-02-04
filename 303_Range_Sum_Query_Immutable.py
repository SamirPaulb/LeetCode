class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.res = [0] * (len(nums) + 1)
        self.data = list(nums)
        for i in range(len(self.data)):
            self.res[i + 1] = self.res[i] + nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.res[j + 1] - self.res[i]

        # Your NumArray object will be instantiated and called as such:
        # numArray = NumArray(nums)
        # numArray.sumRange(0, 1)
        # numArray.sumRange(1, 2)