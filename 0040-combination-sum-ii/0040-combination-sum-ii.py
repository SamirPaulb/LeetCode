class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, target, path):
            if target == 0:
                res.append(path)
                return 
            if i >= len(candidates) or target < 0:
                return 
            dfs(i+1, target - candidates[i], path + [candidates[i]])
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            dfs(i, target, path)
        
        dfs(0, target, [])
        return res