class Solution:
        
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        
        
        
        
        
        
        
        
        
        def cnt(s):
            
            
            
            
            
            
            
            
            ans = 1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            for c in s:
                
                
                
                
                
                
                
                
                
                
                if c == ' ':
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    ans += 1
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            return ans
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        res = 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        for s in sentences:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            res = max(res, cnt(s))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        return res