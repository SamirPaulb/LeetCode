class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = sorted([d/s for d, s in zip(dist, speed)])
        t = 0
        while t < len(time) and t < time[t]:
            t += 1
        return t