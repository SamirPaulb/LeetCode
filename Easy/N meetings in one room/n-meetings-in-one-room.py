#User function Template for python3

class Solution:
    def maximumMeetings(self,n,start,end):
        # code here
        meeting = [(s,e) for s,e in zip(start, end)]
        meeting.sort(key = lambda x:x[1])
        l = 0 
        res = 1
        for r in range(n):
            if meeting[r][0] > meeting[l][1]:
                res += 1
                l = r
            
        return res
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends