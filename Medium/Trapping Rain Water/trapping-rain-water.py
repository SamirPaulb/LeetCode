class Solution:
    #Back-end complete function Template for Python 3
    
    # Function to find the trapped water between the blocks.
    def findWater(self, arr, n): 
      
        # left[i] contains height of tallest bar to the 
        # left of ith bar including itself. 
        left = [0]*n 
      
        # right[i] contains height of tallest bar to 
        # the right of ith bar including itself.
        right = [0]*n 
      
        water = 0
      
        # Storing values of tallest bar from first index till ith index.
        left[0] = arr[0] 
        for i in range( 1, n): 
            left[i] = max(left[i-1], arr[i]) 
      
        # Storing values of tallest bar from last index till ith index.
        right[n-1] = arr[n-1] 
        for i in range(n-2, -1, -1): 
            right[i] = max(right[i+1], arr[i]); 
      
        # Storing the result by choosing the minimum of heights of tallest bar to
        # the right and left of the bar at current index and also subtracting the
        # value of current index to get water accumulated at current index.
        for i in range(0, n): 
            water += min(left[i],right[i]) - arr[i] 
        
        # returning the result.
        return water 
     
    def trappingWater(self, arr,n):
        return self.findWater(arr,n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends