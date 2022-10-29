# https://youtu.be/M0Zay1Qr9ws

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        while (n % 2 == 0) or (n % 3 == 0) or (n % 5 == 0):
            if n % 2 == 0: n = n // 2
            elif n % 3 == 0: n = n // 3
            else: n = n // 5
                
        if n == 1: return True
        return False