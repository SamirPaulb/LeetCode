class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l,r = 0, len(people)-1
        people.sort()
        res = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            res += 1
        return res