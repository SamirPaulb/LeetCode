# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root or k <= 0: return root
        self.k = k
        self.ans = root.val
        def inorder(root):
            if not root: return
            inorder(root.left)
            self.k -= 1
            if self.k == 0: 
                self.ans = root.val
                return
            inorder(root.right)
        
        inorder(root)
        return self.ans

# Time Complexity = O(N)
# Space Complexity = O(1)