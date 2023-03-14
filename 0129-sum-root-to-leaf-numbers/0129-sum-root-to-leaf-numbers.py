# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return [""]
            if not root.left and not root.right: 
                return [str(root.val)]
            arr = []
            left = dfs(root.left)
            if left != [""]:
                for l in left:
                    arr.append(str(root.val) + l)
            right = dfs(root.right)
            if right != [""]:
                for r in right:
                    arr.append(str(root.val) + r)
            return arr
        
        arr = dfs(root)
        # print(arr)
        return sum(int(v) for v in arr)