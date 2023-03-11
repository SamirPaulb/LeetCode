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
        if not head: return None
        prevMid, mid = self.getMid(head)
        if not mid: return None
        nextToMid = mid.next
        mid.next = None
        prevMid.next = None
        root = TreeNode(mid.val)
        if prevMid == mid: return root
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(nextToMid)
        return root
        
    
    def getMid(self, head):
        if not head: return None
        slow, prevslow, fast = head, head, head
        while fast and fast.next:
            prevslow = slow
            slow = slow.next
            fast = fast.next.next
        return prevslow, slow