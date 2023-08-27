import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [str(i) for i in range(1, n+1)]
        fact = math.factorial(n-1)
        k -= 1
        res = ''
        while k:
            i = k//fact
            res += arr[i]
            arr.pop(i)
            k = k % fact
            n -= 1
            fact //= n

        res += ''.join(arr)
        return res