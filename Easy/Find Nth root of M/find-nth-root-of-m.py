#User function Template for python3

class Solution:
	def NthRoot(self, n, m):
		# Code here
		l, r = 0, m
		while l <= r:
		    mid = l + (r-l)//2
		    if mid ** n < m:
		        l = mid + 1
		    elif mid ** n > m:
		        r = mid - 1
		    else:
		        return mid
		return -1
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends