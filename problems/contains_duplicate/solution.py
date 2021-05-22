class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set(nums)
        al = len(a)
        ll = len(nums)
        if ll - al >= 1:
            return True
        else:
            return False