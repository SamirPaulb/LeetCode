class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_i = {}
        prefix_s = []
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            prefix_s.append(s)
            rem = s % k
            if rem == 0 and i > 0: return True
            if rem in rem_i:
                pre_rem = s-prefix_s[rem_i[rem]]
                if pre_rem % k == 0 and i - rem_i[rem] > 1:
                    return True
            else:
                rem_i[rem] = i
        
        return False