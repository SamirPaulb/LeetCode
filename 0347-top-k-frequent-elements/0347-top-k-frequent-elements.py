class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_cnt = {}
        for num in nums:
            if num not in num_cnt: num_cnt[num] = 1
            else: num_cnt[num] += 1
        
        cnt_num = {}
        for num in num_cnt:
            cnt = num_cnt[num]
            if cnt not in cnt_num: cnt_num[cnt] = [num]
            else: cnt_num[cnt].append(num)
        
        res = []
        n = max(num_cnt.values())
        for cnt in range(n, 0, -1):
            if cnt in cnt_num:
                res += cnt_num[cnt]
            if len(res) >= k: break
        
        return res