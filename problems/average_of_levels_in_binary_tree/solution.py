# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Implement Level order traversal and append average of each level = sum(tmp_ans)/len(tmp_ans) in final_ans
        final_ans = []
        q = []
        if not root: return 
        q.append(root)
        while q:
            tmp_ans = []
            for i in range(len(q)):
                node = q.pop(0)
                tmp_ans.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if len(tmp_ans) == 1:
                final_ans.append(float(tmp_ans[0]))
            else:
                final_ans.append(sum(tmp_ans)/len(tmp_ans))
        return final_ans