class Solution:
    def mySqrt(self, x):
        low, high = 0, x
        
        while low <= high:
            mid = (low + high) // 2
            
            if mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
            else:
                return mid
        
        # When there is no perfect square, high is the the value on the left
        # of where it would have been (rounding down). If we were rounding up, 
        # we would return low
        return high