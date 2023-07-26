#User function Template for python3

class Solution:
	def maximize_xor_count(self, n):
		res = 0
		i = 1
		while n:
		    if n&(1) == 0:
		        res += 2**i//2
		    i += 1
            n = n >> 1
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.maximize_xor_count(n)
		print(ans)


# } Driver Code Ends