class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = [0]*(10**5 + 2)
        for i in nums:
            a[i] += 1
        for i in range(len(a)):
            if a[i] > 1: return i
            
        