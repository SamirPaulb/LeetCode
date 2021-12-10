class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def solve(root, tmp, s):
            if not root: return
            if not root.left and not root.right:
                if root.val + s == targetSum:
                    tmp.append(root.val)
                    res.append(tmp)
            solve(root.left, tmp + [root.val], s + root.val)
            solve(root.right, tmp + [root.val], s + root.val)
        
        solve(root, [], 0)
        return res