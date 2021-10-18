class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Note:  *There will be only two majority element*. suppose there are 3 majority element then count of each element will be n/3 and there will be only there 3 unique elements in the array. But question is elements that appear *more than ⌊ n/3 ⌋ times*.
        me1 = -1  # Majority element 1
        me2 = -1  # Majority element 2
        count1 = 0 # Count of MAjority element 1
        count2 = 0 # Count of Majority element 2
        
        for i in nums:
            if me1 == i:
                count1 += 1
            elif me2 == i:
                count2 += 1
            elif count1 == 0:
                me1 = i
                count1 = 1
            elif count2 == 0:
                me2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        ans = []
        if nums.count(me1) > len(nums) // 3: ans.append(me1)
        if nums.count(me2) > len(nums) // 3: ans.append(me2)
        
        return set(ans)