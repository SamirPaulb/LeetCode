class Solution:
    def canPlaceFlowers(self, fb: List[int], n: int) -> bool:
        count = 0
        if len(fb) == 1 and fb[0] == 0:
            count += 1
            fb[0] = 1
            return count >= n
        if fb[0] == 0 and fb[1] == 0:
            fb[0] = 1
            count += 1
        if fb[-1] == 0 and fb[-2] == 0:
            fb[-1] = 1
            count += 1
        print(fb)
        print(count)
        for i in range(1, len(fb)-1):
            if fb[i-1] == 0 and fb[i] == 0 and fb[i+1] == 0:
                fb[i] = 1
                count += 1
            i += 2
        return count >= n