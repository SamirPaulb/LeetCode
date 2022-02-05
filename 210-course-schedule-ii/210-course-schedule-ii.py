class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites: return [i for i in range(numCourses)]
        
        adjacencyList = {i:[] for i in range(numCourses)}
        for num in prerequisites:
            adjacencyList[num[0]].append(num[1])
        
        outBound = {i:0 for i in range(numCourses)}
        for num in prerequisites:
            outBound[num[1]] += 1
        
        q = []
        for i in outBound:
            if outBound[i] == 0: q.append(i)
        
        res = []
        while q:
            a = q.pop()
            res.append(a)
            for i in adjacencyList[a]:
                outBound[i] -= 1
                if outBound[i] == 0: q.append(i)
        
        for i in outBound:
            if outBound[i] != 0: return []
            
        return res[::-1]