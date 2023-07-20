class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in strs:
            if not s: return ''
            i = 0
            while i < len(res):
                
                if res[i] != s[i]:
                    res = s[:i]
                    break
                else:
                    if i >= len(s)-1:
                        res = s
                        break
                    i += 1
                    
        return res