# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        def inorder(root):
            if not root: return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        l = 0
        r = len(arr)-1
        while l < r:
            twoSum = arr[l] + arr[r]
            if twoSum < k:
                l += 1
            elif twoSum > k:
                r -= 1
            else:
                return True
            
        return False