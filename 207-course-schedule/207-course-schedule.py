class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True
        adjacencyList = {i:[] for i in range(numCourses)}
        
        for c in prerequisites:
            adjacencyList[c[0]].append(c[1])
        
        outBound = {i:0 for i in range(numCourses)}
        
        for c in prerequisites:
            outBound[c[1]] += 1
        
        q = []
        for c in outBound:
            if outBound[c] == 0: q.append(c)
        
        while q:
            a = q.pop()
            for c in adjacencyList[a]:
                outBound[c] -= 1
                if outBound[c] == 0: q.append(c)
        
        for c in outBound:
            if outBound[c] != 0: return False
        
        return True