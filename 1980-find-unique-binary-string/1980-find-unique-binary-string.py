class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        numset = set([int(i, 2) for i in nums])
        for i in range(2**n):
            if i not in numset: 
                res = bin(i)[2:]
                return '0' * (n - len(res)) + res