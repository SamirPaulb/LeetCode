class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited_index = set()
        res = 0
        for i in range(len(nums)):
            visited_num = set()
            cur = nums[i]
            cnt = 0
            while cur not in visited_num:
                visited_num.add(cur)
                cnt += 1
                res = max(res, cnt)
                cur = nums[cur]
                if cur in visited_index: break
                visited_index.add(cur)
        return res
    
    
    