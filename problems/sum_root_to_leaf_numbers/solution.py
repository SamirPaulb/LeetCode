class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def binaryTreePath(root, s):
            if not root: return
            if not root.left and not root.right:
                s += str(root.val)
                self.ans += int(s)
                return
            binaryTreePath(root.left, s + str(root.val))
            binaryTreePath(root.right, s + str(root.val))
        
        binaryTreePath(root, "")
        return self.ans