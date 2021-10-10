class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [0] * (10 ** 5 + 1)
        
        for i in nums:
            arr[i] += 1
        
        for i, ch in enumerate(arr):
            if ch > 1: return i
        
        return -1
        