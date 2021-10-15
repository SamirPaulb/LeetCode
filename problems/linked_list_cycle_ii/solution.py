# https://www.youtube.com/watch?v=aIR0s1tY2Vk
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return None
        nodeDic = {}
        node = head
        
        while node and node.next :
            if node in nodeDic: return node
            nodeDic[node] = 1
            node = node.next
        
        return None
        