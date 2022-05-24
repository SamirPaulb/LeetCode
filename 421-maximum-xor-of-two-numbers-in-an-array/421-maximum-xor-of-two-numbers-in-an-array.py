class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = -1  # used to store the value of number at the end

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addNum(self, num):
        cur = self.root
        for i in range(31, -1, -1):
            bit = 1 if num & (1 << i) else 0
            if bit not in cur.children:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
        cur.val = num
                

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.addNum(num)
        
        res = 0
        for num in nums:
            cur = trie.root
            for i in range(31, -1, -1):
                bit = 1 if num & (1 << i) else 0
                if bit == 1:  
                    if 0 in cur.children:
                        cur = cur.children[0]
                    else:
                        cur = cur.children[1]
                else:     # bit == 0
                    if 1 in cur.children:
                        cur = cur.children[1]
                    else:
                        cur = cur.children[0]
                        
            res = max(res, cur.val ^ num)
        
        return res