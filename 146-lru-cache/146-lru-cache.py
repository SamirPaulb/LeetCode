class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = {}
        self.left = ListNode(-1, -1)
        self.right = ListNode(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def makeMRU(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right
    
    def get(self, key: int) -> int:
        if key not in self.dict: return -1
        node = self.dict[key]
        self.remove(node)
        self.makeMRU(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        node = ListNode(key, value)
        self.dict[key] = node
        self.makeMRU(node)
        if len(self.dict) > self.cap:
            lru = self.left.next
            del self.dict[lru.key]
            self.remove(lru)

