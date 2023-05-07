# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque()
        q.append(root)
        flag = False
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node and flag: return False
                if not node: 
                    flag = True
                    continue
                q.append(node.left)
                q.append(node.right)
                
        return True
                