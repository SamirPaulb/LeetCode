class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, min, max):
            if not root: return True
            if not min < root.val < max: return False
            return check(root.left, min, root.val) and check(root.right, root.val, max)
        return check(root, float("-inf"), float("inf"))