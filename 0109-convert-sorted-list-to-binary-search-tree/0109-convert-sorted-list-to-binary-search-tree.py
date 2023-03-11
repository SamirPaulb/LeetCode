# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        def solve(l, r):
            if l > r: return None
            mid = l + (r - l)//2
            root = TreeNode(arr[mid])
            root.left = solve(l, mid-1)
            root.right = solve(mid+1, r)
            return root
        
        return solve(0, len(arr)-1)