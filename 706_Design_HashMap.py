class MyHashMap(object):

    # https://leetcode.com/problems/design-hashmap/discuss/152746/Java-Solution
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.nodes = [None] * self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = hash(key) % self.size
        if self.nodes[index] is None:
            self.nodes[index] = ListNode(-1, -1)
        prev = find(self.nodes[index], key)
        if prev.next is None:
            prev.next = ListNode(key, value)
        else:
            prev.next.val = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = hash(key) % self.size
        if self.nodes[index] is None:
            return -1
        prev = find(self.nodes[index], key)
        if prev.next is None:
            return -1
        else:
            return prev.next.val

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = hash(key) % self.size
        if self.nodes[index] is None:
            return
        prev = find(self.nodes[index], key)
        if prev.next is None:
            return
        prev.next = prev.next.next


def find(bucket, key):
    # find prev node of this key
    node = bucket
    prev = None
    while node is not None and node.key != key:
        prev = node
        node = node.next
    return prev


# Basic node in hash map
class ListNode():

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)