class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        while n != 1:
            a = str(n)
            n = 0
            for i in a:
                n += int(i)**2
            count += 1
            if count > 100: return False
            
        return True