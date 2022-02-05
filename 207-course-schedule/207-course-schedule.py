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
        