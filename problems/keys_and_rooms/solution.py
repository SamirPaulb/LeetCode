class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0]*len(rooms)
        visited[0] = 1
        stack = []
        for e in rooms[0]:
            stack.append(e)
        while len(stack) != 0:
            tmp = stack.pop()
            visited[tmp] = 1
            if len(rooms[tmp]) != 0 and visited[tmp] == 1:
                for j in rooms[tmp]:
                    if visited[j] == 1: continue
                    stack.append(j)
        
        return visited.count(1) == len(rooms)