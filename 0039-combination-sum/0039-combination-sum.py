class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, target, path):
            if target == 0:
                res.append(path)
                return
            if i >= len(candidates) or target < 0:
                return
            dfs(i, target - candidates[i], path + [candidates[i]])
            dfs(i+1, target, path)
        
        dfs(0, target, [])
        return res