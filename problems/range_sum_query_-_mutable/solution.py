class BIT:
    def __init__(self, n):
        self.sums = [0] * (n+1)
    
    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & (-i)
    
    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        return res

class NumArray:
    def __init__(self, nums):
        self.bit = BIT(len(nums))
        for i, num in enumerate(nums):
            self.bit.update(i+1, num)
        self.nums = [0] + nums

    def update(self, i, val):
        self.bit.update(i+1, val - self.nums[i+1])
        self.nums[i+1] = val

    def sumRange(self, i, j):
        return self.bit.query(j+1) - self.bit.query(i)