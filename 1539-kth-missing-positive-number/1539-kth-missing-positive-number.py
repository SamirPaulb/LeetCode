class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arrset = set(arr)
        for i in range(1, 2002):
            if i not in arrset:
                k -= 1
            if k == 0: return i
        
        return -1