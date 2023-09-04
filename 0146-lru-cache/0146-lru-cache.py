class ListNode:
    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.key = key
        self.val = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = ListNode(-2**31, -2**31)
        self.right = ListNode(2**31, 2**31)
        self.left.next = self.right
        self.right.prev = self.left
        self.keyVal = {}
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def makeRecent(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.keyVal: return -1
        node = self.keyVal[key]
        self.remove(node)
        self.makeRecent(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keyVal:
            node = self.keyVal[key]
            self.remove(node)
            node.val = value
            self.makeRecent(node)
        else:
            node = ListNode(key, value)
            self.keyVal[key] = node
            self.makeRecent(node)
            if len(self.keyVal) > self.capacity:
                nodeToRemove = self.left.next
                self.remove(nodeToRemove)
                del self.keyVal[nodeToRemove.key]

