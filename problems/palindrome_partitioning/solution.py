class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def solve(s, path):
            if not s: res.append(path); return
            for i in range(1, len(s)+1):
                if isPalindrome(s[:i]): 
                    solve(s[i:], path + [s[:i]])
        
        def isPalindrome(s): return s == s[::-1]
        
        solve(s, [])
        
        return res