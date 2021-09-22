class Solution:
    def longestValidParentheses(self, s: str) -> int:
        o = c = 0   # o = count of Open Parenthisis "(" , # c = count of close parenthisis ")"
        ans = 0
        for i in range(len(s)):
            if s[i] == "(": o += 1
            else: c += 1
            
            if o == c: ans = max(ans, o+c)
            elif c > o:  # while thaversing from start to end if count of closing parenthesis greter than opening parenthesis => NO valid parenthesis pair exist in that scope.
                o = c = 0
        
        
        o = c = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "(": o += 1
            else: c += 1
            
            if o == c: ans = max(ans, o+c)
            elif o > c:   # While traversing from end to start if count of opening parenthesis greter than count of closing parenthesis => NO valid parenthesis pair exist in that scope.
                o = c = 0
        
        return ans