class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)
        arr = sorted(list(set(hand)))
        i = 0
        while i < len(arr):
            while i < len(arr) and cnt[arr[i]] == 0:
                i += 1
            if i >= len(arr): break
            a = arr[i]
            for j in range(a, a+groupSize):
                cnt[j] -= 1
                if cnt[j] < 0: return False
        
        return True