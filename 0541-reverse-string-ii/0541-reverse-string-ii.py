class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        res = ""
        flag = -1
        for i in range(0, n, k):
            if flag == -1:
                res += s[i:i+k][::-1]
            else:
                res += s[i:i+k]
            flag *= -1
        
        return res