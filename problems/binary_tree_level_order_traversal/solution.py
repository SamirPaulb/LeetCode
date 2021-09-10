# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        final_ans = []
        q = []
        q.append(root)
        while len(q) != 0:
            tmp_ans = []
            for i in range(len(q)):
                node = q.pop(0)
                tmp_ans.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            final_ans.append(tmp_ans)
        return final_ans
    