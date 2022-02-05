class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isPal(s):
            return s == s[::-1]
        
        def solve(s, path):
            if not s:
                res.append(path)
            for i in range(len(s)):
                if isPal(s[:i+1]):
                    solve(s[i+1:], path + [s[:i+1]])
        
        solve(s, [])
        
        return res