class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        q1 = collections.deque(v1.split('.'))
        q2 = collections.deque(v2.split('.'))
        while q1 or q2:
            t1 = int(q1.popleft()) if q1 else 0
            t2 = int(q2.popleft()) if q2 else 0
            if t1 > t2: return 1
            if t1 < t2: return -1
        return 0