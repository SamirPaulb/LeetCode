class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False
        sm = sum(arr)//3
        s = 0
        k = 0
        for i in range(len(arr)):
            s += arr[i]
            if s == sm:
                k += 1
                s = 0
        return k >= 3
    
        