class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = {i : False for i in range(n)}
        visited[0] = True   # as room 0 is unlocked
        
        q = [i for i in rooms[0]]
        while q:
            r = q.pop(0)
            visited[r] = True
            for key in rooms[r]:
                if visited[key] == False:
                    q.append(key)
        
        for i in range(n):
            if visited[i] == False: return False
        
        return True