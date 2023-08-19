from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        p = factorial(n-1)
        arr = [str(i+1) for i in range(n)]
        k -= 1
        res = ""
        while k:
            i = k//p
            res += arr[i]
            # print(n, k, i, arr)
            arr = arr[:i] + arr[i+1:]
            k = k%p
            n -= 1
            p = p//n
        res += ''.join(arr)
        return res