class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_cnt = {}
        rem_cnt[0] = 1
        s = res = 0
        for num in nums:
            s += num
            rem = s % k
            if rem in rem_cnt: 
                res += rem_cnt[rem]
                rem_cnt[rem] += 1
            else:
                rem_cnt[rem] = 1
        
        return res