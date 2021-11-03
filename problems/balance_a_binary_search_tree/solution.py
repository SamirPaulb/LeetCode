class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def inorder(root):
            if not root: return
            if root.left: inorder(root.left)
            arr.append(root.val)
            if root.right: inorder(root.right)
        
        inorder(root)
        
        def binaryTraversal(arr, left, right):
            if left > right: return None
            mid = left + (right - left) // 2
            root = TreeNode(arr[mid])
            root.left = binaryTraversal(arr, left, mid - 1)
            root.right = binaryTraversal(arr, mid + 1, right)
            return root
        
        return binaryTraversal(arr, 0, len(arr) - 1)
        