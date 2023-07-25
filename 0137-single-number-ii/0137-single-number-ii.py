class Solution:
    def singleNumber(self, nums):
        res = 0
        negCount = 0
        for i in range(32):
            s = 0
            for num in nums:
                if num < 0: 
                    negCount += 1
                if (abs(num) >> i) & 1:
                    s += 1
                    s %= 3
            res |= (s << i)

        return -res if negCount%3 else res