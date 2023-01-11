class Solution:
    def partition(self, head, x):
        left = l = ListNode(-1)
        right = r = ListNode(-1)
        while head:
            if head.val < x:
                l.next = head
                l = l.next
            else:
                r.next = head
                r = r.next
            head = head.next
        r.next = None
        l.next = right.next
        return left.next
        