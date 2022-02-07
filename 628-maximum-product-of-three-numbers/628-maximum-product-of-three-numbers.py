class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        '''
        nums.sort()
        # nums = [-10, -7, -5, -1, 2, 4]  => maxproduct = -10 * -7 * 4 = 280
        a = nums[0]*nums[1]*nums[-1]
        b = nums[-1]*nums[-2]*nums[-3]
        
        return max(a, b)
        
        # Time: O(n log(n))
        # space: O(1)
        '''
        
        # Optimize the above solution
        
        smallestTwo = [float("inf")] * 2
        largestThree = [float('-inf')] * 3
        
        for num in nums:
            if num < smallestTwo[0]:
                smallestTwo[0] = num
                smallestTwo.sort(reverse = True)
            if num > largestThree[0]:
                largestThree[0] = num
                largestThree.sort()
        # smallestTwo[0] > smallestTwo[1]
        # largestThree[0] < largestThree[1] < largestThree[2]
        a = smallestTwo[1] * smallestTwo[0] * largestThree[2]
        b = largestThree[2] * largestThree[1] * largestThree[0]
        
        return max(a, b)

# Time: O(N)
# Space: O(1)