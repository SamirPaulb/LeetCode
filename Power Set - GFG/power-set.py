#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		n = len(s)
		res = []
		for i in range(1, 2**n):
		    tmp = ""
		    for j in range(len(s)):
		        if i&(1<<j):
		            tmp += s[j]
		    res.append(tmp)
        return sorted(res)
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends