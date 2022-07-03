# https://youtu.be/7ABFKPK2hD4

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode(0, 0) 
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left    

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev   
    
    def insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = ListNode(key, value)
        self.insert(newNode)
        self.cache[key] = newNode
            
        if len(self.cache) > self.capacity:
            lruNode = self.left.next
            self.remove(lruNode)
            del self.cache[lruNode.key]
        