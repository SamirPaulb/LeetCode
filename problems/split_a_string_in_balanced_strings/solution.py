class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        s = list(s)
        stack = []
        while len(s) != 0:
            if len(stack) == 0:
                stack.append(s[0])
                s.pop(0)
            elif stack[-1] =="L" and s[0] == "R":
                stack.pop(-1)
                s.pop(0)
                if len(stack) == 0:
                    ans += 1
            elif stack[-1] == "R" and s[0] == "L":
                stack.pop(-1)
                s.pop(0)
                if len(stack) == 0:
                    ans += 1
            else:
                stack.append(s[0])
                s.pop(0)
        return ans
            