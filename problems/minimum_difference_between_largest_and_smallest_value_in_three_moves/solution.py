# https://www.youtube.com/watch?v=Ht6hc3UsvY0
'''
nums.sort() this sort() function internaly use Quick Sort
sort() function has a O(n log(n)) time complexity
'''
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n <= 4: return 0  # if lenght == 4 then change 3 elements to one element
        res = nums[-1] - nums[0]
        for i in range(4):   # this is of constant time complexity
            res = min(res, nums[n-1-3+i] - nums[i])
        return res
        
# as the sort function is using O(n log(n)) time and No extra spaces is taken so,
# Time Complexity = O(n log(n))
# Space Complexity = O(1)