class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def helper(lock):
            arr = []
            for i in range(4):
                lock1 = lock[:i] + str((int(lock[i])+1)%10) + lock[i+1:]
                lock2 = lock[:i] + str((int(lock[i])-1)%10) + lock[i+1:]
                arr.append(lock1)
                arr.append(lock2)
            return arr

        deadends = set(deadends)
        q = collections.deque([('0000', 0)])
        visited = set()
        while q:
            lock, turns = q.popleft()
            if lock in deadends or lock in visited: continue
            visited.add(lock)
            if lock == target: return turns
            for newLock in helper(lock):
                if newLock in deadends: continue
                q.append((newLock, turns+1))
        return -1
