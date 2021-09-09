'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = head # c = Current Node
        p = None # p = Previous Node
        n = None # n = Next Node of Current
        while c != None:
            n = c.next
            c.next = p
            p = c
            c = n
        return p
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseLinkedList(c, p, n):
            if c == None: return p
            n = c.next
            c.next = p
            p = c
            c = n
            return reverseLinkedList(c, p, n)
        return reverseLinkedList(head, None, None)