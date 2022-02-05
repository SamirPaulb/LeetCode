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
        outBound = {i:0 for i in range(numCourses)}
        for num in prerequisites:
            outBound[num[1]] += 1
        # outbound = [0:0, 1:1, 2:1, 3:1, 4:2]
        q = []
        for i in outBound:
            if outBound[i] == 0: q.append(i)
        while q:
            a = q.pop()
            for i in adjacencyList[a]:
                outBound[i] -= 1
                if outBound[i] == 0: q.append(i)
        
        for i in outBound:
            if outBound[i] != 0: return False
        
        return True
    
    
    
'''
Test cases:

2
[[1,0]]
2
[[1,0],[0,1]]
1
[]
5
[[1,4],[2,4],[3,1],[3,2]]

'''