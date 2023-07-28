class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me = '#'
        mc = 1
        
        for num in nums:
            if me != num:
                mc -= 1
            else:
                mc += 1
            if mc == 0:
                me = num
                mc = 1
        
        return me