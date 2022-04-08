class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        def dfs(arr, path):
            if not arr:
                res.add(tuple(path))
            for i in range(len(arr)):
                dfs(arr[:i] + arr[i+1:], path + [arr[i]])
        
        dfs(nums, [])
        
        return res