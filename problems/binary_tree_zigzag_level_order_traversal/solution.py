# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # First we are gonna find the level order traversal
        # Then print in zigzag manner
        levelorder = []
        q = []
        
        if not root: return q
        q.append(root)
        
        while q:
            tmp_level = []
            for i in range(len(q)):
                node = q.pop(0)
                tmp_level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            levelorder.append(tmp_level)
        
        zigzag = 0  # 0 = left to right traversal
        for i in range(len(levelorder)):
            if zigzag == 0:
                zigzag = 1  # 1 = right to left traversal
            else:
                levelorder[i] = levelorder[i][::-1]
                zigzag = 0
        
        return levelorder
        
        
        
        
        