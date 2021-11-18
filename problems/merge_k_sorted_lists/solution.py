class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        while len(lists) > 1:
            lists[0] = self.merge2SortedLists(lists[0], lists[1])
            lists.pop(1)
        
        return lists[0]
    
    def merge2SortedLists(self, l1, l2):
        if not l1 or not l2: return l1 or l2
        if l1.val <= l2.val: a, b = l1, l2
        else: a, b = l2, l1
        ans = a
        while a or b:
            if not a.next: 
                a.next = b
                return ans
            if not b: return ans
            if a.next.val <= b.val: a = a.next
            else:
                tmp = a.next
                a.next = b
                b = tmp
                a = a.next
                
        
        