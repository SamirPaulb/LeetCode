class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []
        
        def dfs(start, path, target):
            if target == 0: res.append(path); return
            if start >= n or target < 0: return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]: continue
                dfs(i+1, path + [candidates[i]], target - candidates[i])
        
        dfs(0, [], target)
        return res