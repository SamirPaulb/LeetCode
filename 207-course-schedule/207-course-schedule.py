class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ajList = {}
        
        for i in range(len(prerequisites)):
            a = prerequisites[i][0]
            b = prerequisites[i][1]
            # a is dependent on b (ie. to take a we have to take b first)
            if a not in ajList: ajList[a] = [b]
            else: ajList[a].append(b)
                
            if b not in ajList: ajList[b] = []
        # [[1,4],[2,4],[3,1],[3,2]]
        # ajList = {1:[4], 2:[4], 3:[1,2], 4:[]}
        # [[1,0],[0,1]]
        # ajList = {1:[0], 0:[1]}
        takenCourses = set()
        visited = set()
        
        def canTake(c):
            if c in takenCourses: return True
            if c in visited: return False
            visited.add(c)
            if len(ajList[c]) > 0:
                for i in ajList[c]:
                    if canTake(i) == False: return False
            takenCourses.add(c)
            return True
        
        for c in ajList:
            if canTake(c) == False: return False
            visited.add(c)
            takenCourses.add(c)
            
        return True
    
    
    
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0: return True
        adjacencyList = {i : [] for i in range(numCourses)} 
        for num in prerequisites:
            if num[0] not in adjacencyList: adjacencyList[num[0]] = [num[1]]
            else: adjacencyList[num[0]].append(num[1])
        # BFS
        # outBound = number of elements dependent on the current element => course to be completed before 
        # eg. for [[0,1], [0,2], [1,3], [1,4], [3,4]] outbound of 4 is 2, because 1 and 3 is dependent on 4
        # outBound of 2 is 1, because 0 is dependent on 2 => to complete 0, 2 needs to complete first
        outBound = [[i, 0] for i in range(numCourses)]
        for num in prerequisites:
            outBound[num[1]][1] += 1
        # outbound = [[0,0], [1,1], [2,1], [3,1], [4,2]]
        q = []
        for i in outBound:
            if i[1] == 0: q.append(i[0])
        while q:
            a = q.pop()
            for i in adjacencyList[a]:
                outBound[i][1] -= 1
                if outBound[i][1] == 0: q.append(i)
        
        for i in outBound:
            if i[1] != 0: return False
        
        return True
    
        