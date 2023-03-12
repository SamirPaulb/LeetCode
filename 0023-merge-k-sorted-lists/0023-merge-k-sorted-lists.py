# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        while len(lists) > 1:
            l1 = lists.pop()
            l2 = lists.pop()
            mergedList = self.mergeSort(l1, l2)
            lists.append(mergedList)
        return lists[0]
        
    def mergeSort(self, l1, l2):
        if not l1 or not l2: return l2 or l1
        if l1.val <= l2.val: a = l1; b = l2
        else: a = l2; b = l1
        head = a
        while a or b:
            if not a.next:
                a.next = b
                break
            if not b: break
            
            if a.next.val > b.val:
                tmp = a.next
                a.next = b
                b = tmp
            a = a.next
        
        return head
                
                
                