class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        LL= []
        for i in range(len(nums)):
            s=0
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    continue
                elif nums[j]< nums[i]:
                    s += 1
            LL.append(s)
        return LL
        
                