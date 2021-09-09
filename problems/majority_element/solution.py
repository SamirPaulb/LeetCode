class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = list(set(nums))
        for i in a:
            if nums.count(i) > len(nums)//2: 
                print(i)
                return i