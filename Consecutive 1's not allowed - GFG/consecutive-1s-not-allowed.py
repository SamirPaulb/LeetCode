#User function Template for python3
class Solution:

	def countStrings(self,n):
    	# code here
    	if n == 1: return 2
        a = 1
        b = 2
        for i in range(2, n+1):
            p = a + b
            a = b
            b = p
        return p % (10**9 + 7)
    	
    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
# } Driver Code Ends