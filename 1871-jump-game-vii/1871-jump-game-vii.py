class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        furthest = 0
        
        while q:
            i = q.popleft()
            start = max(i+minJump, furthest+1)
            for j in range(start, min(i+maxJump+1, len(s))):
                if s[j] == '0':
                    if j == len(s)-1:
                        return True
                    q.append(j)
            furthest = i+maxJump
            
        return False
                