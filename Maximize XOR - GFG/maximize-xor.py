'''
Step 1:- Just find out the position of unset bit in number.
Step 2:- Suppose, if unset bit at i'th position then add (2^i)/2 in result variable
         /2 as that bit will not be consider and all permutation of right-side bits will 
         be lesser.
Step 3:- Right shift number n one time
Step 4:- continue till num become zero(0)
'''


class Solution:
	def maximize_xor_count(self, n):
		res = 0
		i = 1
		while n:
		    if n&1 == 0:
		        res += (2**i)//2
		    i += 1
            n = n >> 1
        return res

# Time: O(32)
# Space: O(1)



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