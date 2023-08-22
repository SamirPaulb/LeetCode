class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        me1 = ""
        mc1 = 0
        me2 = ""
        mc2 = 0
        for num in nums:
            if me1 == num:
                mc1 += 1
            elif me2 == num:
                mc2 += 1
            elif mc1 == 0:
                me1 = num
                mc1 = 1
            elif mc2 == 0:
                me2 = num
                mc2 = 1
            else:
                mc1 -= 1
                mc2 -= 1
        
        res = set()
        if nums.count(me1) > len(nums)//3: res.add(me1)
        if nums.count(me2) > len(nums)//3: res.add(me2)
        return res
