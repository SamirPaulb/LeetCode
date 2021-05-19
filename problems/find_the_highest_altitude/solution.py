class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = 0
        L = [0]
        for i in range(len(gain)):
            s = s+ gain[i]
            L.append(s)
        return max(L)
            