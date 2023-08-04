class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr = []
        for i in range(len(s)):
            d = abs(ord(s[i]) - ord(t[i]))
            arr.append(d)
        
        l = res = curSum = 0
        for r in range(len(s)):
            curSum += arr[r]
            while curSum > maxCost:
                curSum -= arr[l]
                l += 1
            res = max(res, r-l+1)
        
        return res