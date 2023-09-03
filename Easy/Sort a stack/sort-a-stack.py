class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        if not s: return 
        tmp = s.pop()
        self.Sorted(s)  
        self.helper(s, tmp)
        return s
    
    def helper(self, stack, tmp):
        if stack and stack[-1] > tmp:
            top = stack.pop()
            self.helper(stack, tmp)
            stack.append(top)
        else:
            stack.append(tmp)
        return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends