class Solution:
    def canPlaceFlowers(self, fb: List[int], n: int) -> bool:
        fb = [0] + fb + [0]
        i, cnt = 1, 0
        for i in range(1, len(fb)-1):
            if fb[i-1] == fb[i] == fb[i+1] == 0:
                fb[i] = 1
                cnt += 1
        return cnt >= n        