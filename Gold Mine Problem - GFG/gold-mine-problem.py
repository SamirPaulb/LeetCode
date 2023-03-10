# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        # code here
        if n == 1: return sum(M[0])
        for c in range(1, m):
            for r in range(n):
                if r == 0:
                    M[r][c] += max(M[r][c-1], M[r+1][c-1])
                elif r == n-1:
                    M[r][c] += max(M[r][c-1], M[r-1][c-1])
                else:
                    M[r][c] += max(M[r-1][c-1], M[r][c-1], M[r+1][c-1])
        res = 0
        for r in range(n):
            res = max(res, M[r][-1])
        return res
        

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends