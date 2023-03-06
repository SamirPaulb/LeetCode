class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        dp = {}
        
        def cal(sign, left, right):
            if sign == '+': return left + right
            elif sign == '-': return left - right
            else: return left * right
        
        def solve(s):
            if s.isdigit(): return [int(s)]
            if s in dp: return dp[s]
            ans = []
            for i in range(len(s)):
                if s[i] in "+-*":
                    for left in solve(s[:i]):
                        for right in solve(s[i+1:]):
                            ans.append(cal(s[i], left, right))
            dp[s] = ans
            return ans
        
        return solve(s)