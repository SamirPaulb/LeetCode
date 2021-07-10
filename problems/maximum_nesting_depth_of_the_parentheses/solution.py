class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_value = 0
        for i in range(len(s)):
            if s[i] == "(":
                count += 1
                
            elif s[i] == ")":
                count -= 1
            
            max_value = max(max_value, count)
            
        return max_value