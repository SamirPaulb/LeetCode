class TrieNode:
    def __init__(self):
        self.children = {}
        self.fin_val = -1
    
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, val):
        ptr = self.root
        for x in range(31, -1, -1):
            digit = 1 if (val & 1 << x) else 0
            if digit not in ptr.children:
                ptr.children[digit] = TrieNode()
            ptr = ptr.children[digit]
        ptr.fin_val = val


    def max_xor(self, A):
        g_max = 0
        for x in range(len(A)):
            ptr = self.root
            curr = A[x]
            for y in range(31, -1, -1):
                digit = 1 if (curr & 1 << y) else 0
                if digit == 0:
                    if 1 in ptr.children:
                        ptr = ptr.children[1]
                    else:
                        ptr = ptr.children[0]
                else:
                    if 0 in ptr.children:
                        ptr = ptr.children[0]
                    else:
                        ptr = ptr.children[1]
            g_max = max(g_max, ptr.fin_val ^ curr)
        return g_max
            
        
        
class Solution:
    # @param A : list of integers
    # @return an integer
    def findMaximumXOR(self, A):
        t = Trie()
        for x in A:
            t.insert(x)
        return t.max_xor(A)