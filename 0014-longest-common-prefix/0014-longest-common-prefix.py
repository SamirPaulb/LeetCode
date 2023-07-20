class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            k = strs[0][i]
            n = 0
            for s in strs:
                if i < len(s) and s[i] == k:
                    n += 1
            if n == len(strs):
                res += k
            else:
                break
        
        return res