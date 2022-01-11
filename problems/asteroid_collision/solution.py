class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(asteroids)):
            curr = asteroids[i]
            
            while stack and curr < 0 and stack[-1] > 0:
                if abs(curr) < stack[-1]: 
                    break
                elif abs(curr) > stack[-1]:
                    stack.pop()
                else:   # abs(curr) == stack[-1]
                    stack.pop()
                    break
            else:
                stack.append(curr)
        
        return stack
    
    
    
    

    
'''
[5,10, 15]
[8,-8]
[10,2,-5]
[-2,-2,-2,1]
[-2,10,-5,21,-15,9]
[-2,-2,1,-2]
'''    