#User function Template for python3

class Solution:
    def colName (self, n):
        # your code here
        res = ''
        while n > 0:
            r = n%26
            if r == 0: 
                res = 'Z' + res
                n = (n-1)//26
            else:
                res = chr(64 + r) + res
                n = n//26
        
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends