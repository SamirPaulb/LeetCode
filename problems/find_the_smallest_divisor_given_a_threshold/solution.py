
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def getSum(divisor, xs):
            return sum([x // divisor + 1 if x % divisor else x // divisor for x in xs])
		
        left, right = 1, 10 ** 6
        while left + 1 < right:
            mid = (left + right) // 2            
            if getSum(mid, nums) > threshold: 
                left = mid
            else: 
                right = mid
        
        return left if getSum(left, nums) <= threshold else right