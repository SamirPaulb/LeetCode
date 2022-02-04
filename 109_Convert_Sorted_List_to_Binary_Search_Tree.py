# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # convert to list
    # def __init__(self):
    #     self.nodelist = []
    #
    # def sortedListToBST(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: TreeNode
    #     """
    #     if head is None:
    #         return None
    #     size = 0
    #     pos = head
    #     while pos is not None:
    #         self.nodelist.append(pos)
    #         pos = pos.next
    #         size += 1
    #     return self.sortList(0, size - 1)
    #
    # def sortList(self, start, end):
    #     if start > end:
    #         return None
    #     mid = (start + end) / 2
    #     current = TreeNode(self.nodelist[mid].val)
    #     current.left = self.sortList(start, mid - 1)
    #     current.right = self.sortList(mid + 1, end)
    #     return current

    # point in recursive function
    def __init__(self):
        self.node = None
    
    def sortedListToBST(self, head):
        # Bottom-up recursion O(n) and O(lgn)
        if head is None:
            return head
        size = 0
        pos = self.node = head
        while pos is not None:
           pos = pos.next
           size += 1
        return self.inorderHelper(0, size - 1)
    
    def inorderHelper(self, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        # left side and move
        left = self.inorderHelper(start, mid - 1)
        # move and create
        root = TreeNode(self.node.val)
        root.left = left
        self.node = self.node.next
        # right side and move
        root.right = self.inorderHelper(mid + 1, end)
        return root

    # two point
    # O(nlgn) and O(n)
    # def sortedListToBST(self, head):
    #     if head is None:
    #         return head
    #     return self.toBST(head, None)

    # def toBST(self, head, tail):
    #     fast = slow = head
    #     if head == tail:
    #         return None
    #     while fast != tail and fast.next != tail:
    #         fast = fast.next.next
    #         slow = slow.next
    #     root = TreeNode(slow.val)
    #     root.left = self.toBST(head, slow)
    #     root.right = self.toBST(slow.next, tail)
    #     return root
        




