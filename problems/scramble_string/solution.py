class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        mp = {}
        def solve(a, b):
            n = len(a)
            if a == b: return True
            if len(a) <= 1: return False
            key = a + "-" + b
            if key in mp: return mp[key]
            flag = False
            for i in range(1, len(a)):
                swap = solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i])
                noswap = solve(a[:i], b[:i]) and solve(a[i:], b[i:])
                if swap or noswap:
                    flag = True
                    break
                    
            mp [key] = flag
            return flag
        
        return solve(s1, s2)