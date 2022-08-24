# https://leetcode.com/problems/minimum-window-substring/
# https://youtu.be/jSto0O4AJbM

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = {i:0 for i in t}
        for i in t: tDict[i] += 1
        sDict = {i:0 for i in t}

        have = 0
        need = len(tDict.keys())
        res = s*30
        l, r = 0, 0
        while r < len(s):
            if s[r] in sDict:
                sDict[s[r]] += 1
                if sDict[s[r]] == tDict[s[r]]:
                    have += 1
            r += 1
            while l < r and have == need:
                if s[l] in sDict:
                    if r - l < len(res):
                        res = s[l : r]
                    sDict[s[l]] -= 1
                    if sDict[s[l]] < tDict[s[l]]: 
                        have -= 1
                l += 1
        
        return res if res != s*30 else ""
        
                
            
# Time: O(N)
# Space: O(N)