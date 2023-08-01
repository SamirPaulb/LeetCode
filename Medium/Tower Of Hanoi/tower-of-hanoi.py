# User function Template for python3

class Solution:
    def toh(self, n, from_rod, to_rod, aux_rod):
        if n == 0: 
            return 0
        moves = 1
        moves += self.toh(n-1, from_rod, aux_rod, to_rod)
        print("move disk", n, "from rod", from_rod, "to rod", to_rod)
        moves += self.toh(n-1, aux_rod, to_rod, from_rod)
        return moves
        
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends