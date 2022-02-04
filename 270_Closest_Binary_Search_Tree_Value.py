# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def closestValue(self, root, target):
    #     """
    #     :type root: TreeNode
    #     :type target: float
    #     :rtype: int
    #     """
    #     # brute force, Search all
    #     return self.closestValue_helper(root, target, 21474483647)

    
    # def closestValue_helper(self, root, target, curr_min):
    #     if root is None:
    #         return curr_min
    #     if abs(root.val - target) < abs(curr_min - target):
    #         curr_min = root.val
    #     left_min = self.closestValue_helper(root.left, target, curr_min)
    #     right_min = self.closestValue_helper(root.right, target, curr_min)
    #     if abs(left_min - target) < abs(right_min - target):
    #         return left_min
    #     else:
    #         return right_min

    # def closestValue(self, root, target):
    #     # Iteratively compare root result with current kid's result (left or right)
    #     path = []
    #     while root:
    #         path += root.val,
    #         root = root.left if target < root.val else root.right
    #     return min(path, key=lambda x: abs(target - x))

    def closestValue(self, root, target):
        # compare kids' result with root
        kid = root.left if target < root.val else root.right
        if not kid:
            return root.val
        kid_min = self.closestValue(kid, target)
        return min((kid_min, root.val), key=lambda x: abs(target - x))

