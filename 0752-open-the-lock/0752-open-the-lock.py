class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends: 
            return -1
        visited = set()
        q = collections.deque()
        q.append(['0000', 0])
        
        def children(lock):
            arr = []
            for i in range(4):
                cur = int(lock[i])
                q.append([lock[:i] + str((cur+1)%10) + lock[i+1:], turns + 1])
                q.append([lock[:i] + str((cur-1)%10) + lock[i+1:], turns + 1])
            return arr
            
            
        while q:
            lock, turns = q.popleft()
            if lock == target: return turns
            if lock in deadends or lock in visited: continue
            visited.add(lock)
            n = len(q)
            for child in children(lock):
                if child not in deadends and child not in visited:
                    visited.add(child)
                    q.append([child, turns+1])
        
        return -1
                    
            