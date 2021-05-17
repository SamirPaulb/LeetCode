class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        a = [(start + 2*i)for i in range(n)]
        mul = a[0]
        for i in range(1, n):
            mul = mul ^ a[i]
        
        return mul
            
        