class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return 
        if not head.next: return TreeNode(head.val)
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        def binaryTraversal(arr, left, right):
            if left > right: return None
            mid = left + (right - left) // 2
            root = TreeNode(arr[mid])
            root.left = binaryTraversal(arr, left, mid - 1)
            root.right = binaryTraversal(arr, mid + 1, right)
            return root
        
        return binaryTraversal(arr, 0, len(arr) - 1)
