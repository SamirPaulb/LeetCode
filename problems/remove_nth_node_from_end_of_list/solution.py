class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None
        if not head.next and n == 1: return None
        a = head
        b = head
        length = 1
        while a.next:
            a = a.next
            length += 1
        #print(length)
        if n == length:
            return head.next
        i = 1
        while b.next and i < length - n:
            b = b.next
            i += 1
        tel = None
        if b.next:
            tel = b.next.next
        b.next.next = None
        b.next = tel
        
        return head
        