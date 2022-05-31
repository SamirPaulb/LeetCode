class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = {chr(i):0 for i in range(97, 123)}
        for i in s:
            dicS[i] += 1
        
        dicT = {chr(i):0 for i in range(97, 123)}
        for i in t:
            dicT[i] += 1
        
        return dicS == dicT