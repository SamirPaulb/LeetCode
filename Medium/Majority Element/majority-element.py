#Back-end complete function Template for Python 3

class Solution:
    # use linear search to compute candidate for majority element
    def findCandidate(self, A):
        maj_index = 0
        count = 1
        for i in range(len(A)):
            if A[maj_index] == A[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj_index = i
                count = 1
        return A[maj_index]
        
    # Function to check if the candidate occurs more than n/2 times
    def isMajority(self, A, cand):
        count = 0
        for i in range(len(A)):
            if A[i] == cand:
                count += 1
        if count > len(A)/2:
            return True
        else:
            return False
    
    def majorityElement(self, A,N):
        cand = self.findCandidate(A)
    
        # Print the candidate if it is Majority
        if self.isMajority(A, cand) == True:
            return cand
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends