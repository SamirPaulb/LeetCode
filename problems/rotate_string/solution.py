class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal: return True
        n = len(s)
        s = list(s)
        goal = list(goal)
        for i in range(n):
            s.append(s.pop(0))
            if s == goal: return True
        return False