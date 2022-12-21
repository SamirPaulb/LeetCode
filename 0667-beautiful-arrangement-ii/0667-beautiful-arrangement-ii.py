class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        arr = [i for i in range(2, n+1)]
        i = 1
        res = [1]
        while k > 1:
            a = i - k
            b = i + k
            if a in arr:
                res.append(a)
                i = a
            else:
                res.append(b)
                i = b
            arr.remove(i)
            k -= 1
        
        return res + arr