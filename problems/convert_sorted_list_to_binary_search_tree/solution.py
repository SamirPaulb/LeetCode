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
        if not head: return
        if not head.next: return TreeNode(head.val)
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        def binarysearch(arr, left, right):
            if left > right: return 
            mid = left + (right - left) // 2
            root = TreeNode(arr[mid])
            root.left = binarysearch(arr, left, mid - 1)
            root.right = binarysearch(arr, mid + 1, right)
            return root
    
        return binarysearch(arr, 0, len(arr) - 1)
            
            
            
            
            
            