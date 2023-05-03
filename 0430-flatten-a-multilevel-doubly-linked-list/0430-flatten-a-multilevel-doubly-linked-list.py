"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return 
        cur = head
        while cur:
            if cur.child:
                newll = self.flatten(cur.child)
                cur.child = None
                cl = newll
                while cl.next:
                    cl = cl.next
                if cur.next:
                    cur.next.prev = cl
                    cl.next = cur.next
                cur.next = newll 
                newll.prev = cur
            cur = cur.next
        return head
            