class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # while traversing nums I will make nums[nums[i]-1] negative so that if I again encounter nums[i] again i can found it repeated
        #  constant space O(1)
        res = []
        
        for i in range(len(nums)):
            cur = abs(nums[i]) # as i am multiplying with -1 so absolute value
            if nums[cur - 1] < 0: res.append(cur)
            else:
                nums[cur - 1] *= -1
        
        return res
# Time: O(N)
# Space: O(1)
        
        
        
        
'''        
        hashmap = {}
        res = []
        for num in nums:
            if num in hashmap:
                if hashmap[num] == 1:
                    res.append(num)
            else:
                hashmap[num] = 1
        
        return res

# Time: O(N)
# Space: O(N)
'''