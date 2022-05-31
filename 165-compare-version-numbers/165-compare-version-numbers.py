class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        i = 0
        j = 0
        while i < len(v1) or j < len(v2):
            n1 = 0
            k = i
            if k < len(v1):
                while k < len(v1) and v1[k] != '.':
                    k += 1
                n1 = int(v1[i:k])
            i = k + 1
            
            n2 = 0
            k = j 
            if k < len(v2):
                while k < len(v2) and v2[k] != '.':
                    k += 1
                n2 = int(v2[j:k])
            j = k + 1
            
            if n1 < n2: return -1
            if n1 > n2: return 1
        
        return 0