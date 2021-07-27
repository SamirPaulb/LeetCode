class Solution:
    def specialArray(self, nums: List[int]) -> int:
        m = max(nums)
        for i in range(1, m+1):
            cnt = 0
            for itm in nums:
                if itm >= i:
                    cnt += 1
            if cnt == i:
                return cnt
        return -1