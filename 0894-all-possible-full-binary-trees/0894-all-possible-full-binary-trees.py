# https://leetcode.com/problems/all-possible-full-binary-trees/
# https://youtu.be/nZtrZPTTCAo
'''
Eg. N == 9

left sub-tree can have 1 node and right sub-tree can have 7 nodes
left sub-tree can have 3 node and right sub-tree can have 5 node
left sub-tree can have 5 node and right sub-tree can have 3 node
left sub-tree can have 7 node and right sub-tree can have 1 node
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0:[], 1:[TreeNode(0)]}
        def backtrack(n):
            if n in dp:
                return dp[n]
            res = []
            for l in range(1, n):
                r = n - l - 1
                leftTrees = backtrack(l)
                rightTrees = backtrack(r)
                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            
            dp[n] = res
            return res
        
        return backtrack(n)