class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = res = 0
        cnt = {0:1}
        for num in nums:
            s += num
            if s-k in cnt:
                res += cnt[s-k]
            if s in cnt: cnt[s] += 1
            else: cnt[s] = 1
        
        return res