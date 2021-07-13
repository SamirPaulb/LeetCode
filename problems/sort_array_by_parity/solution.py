class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = [i for i in nums if i%2 == 0] + [i for i in nums if i %2!= 0]
        return ans
        