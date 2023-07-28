class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        me1 = -10**9-2
        mc1 = 0
        me2 = -10**9-2
        mc2 = 0
        
        for num in nums:
            if num == me1:
                mc1 += 1
            elif num == me2:
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
        # print(me1, me2)
        if me1 == me2: return [me1]
        elif me1 == '#' or me2 == '#': return me2 or me1
        mc1, mc2 = nums.count(me1), nums.count(me2)
        if mc1 > len(nums)//3 and mc2 > len(nums)//3:
            return [me1, me2]
        if mc1 > len(nums)//3:
            return [me1]
        if mc2 > len(nums)//3:
            return [me2]
        return []