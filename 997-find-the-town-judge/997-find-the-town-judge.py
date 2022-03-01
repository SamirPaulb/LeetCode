class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustOthers = {(i+1):[] for i in range(n)}
        trustedByOthers = {(i+1):[] for i in range(n)}
        
        for a in trust:
            trustOthers[a[0]].append(a[1])
            trustedByOthers[a[1]].append(a[0])
        
        for i in range(1, n+1):
            if not trustOthers[i] and len(trustedByOthers[i]) == n-1:
                return i
        
        return -1