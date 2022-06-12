class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        dic = {}
        for m in mappings:
            if m[0] not in dic:
                dic[m[0]] = {m[1]}
            else:
                dic[m[0]].add(m[1])
        
        for i in range(len(s)-len(sub)+1):
            j = 0
            while j < len(sub) and (s[i+j] == sub[j] or 
                                    (sub[j] in dic and s[i+j] in dic[sub[j]])):
                j += 1

            if j == len(sub): return True
        
        return False
    