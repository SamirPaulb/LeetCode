class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr_len = len(nums)
        set_len = len(set(nums))
        
        return arr_len != set_len
    