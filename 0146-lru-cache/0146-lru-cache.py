class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.keyval = {}
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        
        self.left.next = self.right
        self.right.prev = self.left
    
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def makeRecent(self, node):
        node.next = self.right
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.keyval:
            node = self.keyval[key]
            self.delete(node)
            self.makeRecent(node)
            return node.val
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyval:
            node = self.keyval[key]
            self.delete(node)
            self.makeRecent(node)
            node.val = value
        else:
            node = Node(key, value)
            self.makeRecent(node)
            self.keyval[key] = node
            if len(self.keyval) > self.size:
                delnode =  self.left.next
                self.delete(delnode)
                del self.keyval[delnode.key]