class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res, tmp = [], []
        def dfs(root, sum, tmp, res):
            if not root: return
            if not root.left and not root.right and sum == root.val:
                tmp.append(root.val)
                res.append(tmp)
            else:
                dfs(root.left, sum - root.val, tmp + [root.val], res)
                dfs(root.right, sum - root.val, tmp + [root.val], res)
                
        dfs(root, targetSum, tmp, res)
        return res
        
        