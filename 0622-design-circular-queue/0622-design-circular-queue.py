class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.maxSize = k
        self.curSize = 0

    def enQueue(self, value: int) -> bool:
        newNode = ListNode(value)
        if self.isEmpty(): 
            self.head = self.tail = newNode
        else:
            if self.isFull(): return False
            self.tail.next = newNode
            self.tail = self.tail.next
        self.curSize += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = self.head.next
        self.curSize -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.curSize == 0

    def isFull(self) -> bool:
        return self.curSize == self.maxSize


# Time: O(1)
# Space: O(k)