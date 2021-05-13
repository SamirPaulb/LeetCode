class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_val = 0 
        for i in s:
            if i == "(":
                count +=1
                if count> max_val:
                    max_val = count
            if i == ")":
                count -= 1
        return max_val
    
    
            
        
        
        
        