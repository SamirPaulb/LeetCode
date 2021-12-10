class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me, count = -1, 0
        
        for i in nums:
            if me == i: count += 1
            if count > 0 and me != i: count -= 1
            if count == 0: me = i; count = 1
        
        if nums.count(me) >= len(nums) // 2: return me
        return -1