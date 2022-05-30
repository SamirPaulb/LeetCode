class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.dic:
            self.remove(self.dic[key])
            self.makeRecent(self.dic[key])
            return self.dic[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
            self.dic[key] = ListNode(key, value)
            self.makeRecent(self.dic[key])
        else:
            if len(self.dic) == self.capacity:
                del self.dic[self.head.key]
                self.remove(self.head)
            self.dic[key] = ListNode(key, value)
            self.makeRecent(self.dic[key])
        
    def remove(self, node):
        if self.head.key == node.key:
            self.head = self.head.next
        elif self.tail and self.tail.key == node.key:
            self.tail = self.tail.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        
    def makeRecent(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node