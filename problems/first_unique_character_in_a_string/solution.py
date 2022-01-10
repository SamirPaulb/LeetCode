class Solution:
    def firstUniqChar(self, s: str) -> int:
        countDic = {}
        
        for i in range(len(s)):
            if s[i] not in countDic:
                countDic[s[i]] = 1
            else:
                countDic[s[i]] += 1
        
        found = False
        for i in countDic:
            if countDic[i] == 1:
                found = i
                break
        
        if found == False: return -1
        
        for i in range(len(s)):
            if s[i] == found: return i