class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            total = sum([int(i)**2 for i in str(n)])
            if total == 1:
                return True
            if total in visited:
                return False
            visited.add(total)
            n = total

            