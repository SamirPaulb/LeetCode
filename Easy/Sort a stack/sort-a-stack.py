class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        if not s: return []
        top = s.pop()
        self.sorted(s)
        self.insert(s, top)
        return s
    
    def insert(self, s, top):
        if not s: 
            s.append(top)
            return
        elif top >= s[-1]:
            s.append(top)
            return
        else:
            tmp = s.pop()
            self.insert(s, top)
            s.append(tmp)
            return
            
            
            
        
        
        
        
        
        


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends