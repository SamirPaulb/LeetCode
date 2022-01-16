import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        
        a = math.log(n) / math.log(2)
        a = round(a)
        return 2**a == n