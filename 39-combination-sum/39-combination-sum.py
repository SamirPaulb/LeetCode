class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(candidates)
        
        def dfs(i, path, target):
            if target == 0: res.add(tuple(path))
            if target < 0 or i >= n: return
            for i in range(i, n):
                dfs(i+1, path + [candidates[i]], target - candidates[i])
                dfs(i, path + [candidates[i]], target - candidates[i])
        
        dfs(0, [], target)
        return list(res)
    
    