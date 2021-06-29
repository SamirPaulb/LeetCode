class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        win_start = 0
        num_flip = 0
        res = 0
        for win_end in range(len(nums)):
            num_flip += (nums[win_end] == 0)
            
            while(num_flip > k):
                num_flip -= (nums[win_start] == 0)
                win_start += 1
            res = max(res, win_end - win_start + 1)

        return res
