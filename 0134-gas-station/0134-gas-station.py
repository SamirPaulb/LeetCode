class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gc = [g-c for g,c in zip(gas, cost)]
        print(gc, sum(gc))
        if sum(gc) < 0: return -1
        s, res = 0, 0
        for i in range(len(gc)):
            s += gc[i]
            if s < 0: 
                res = i+1
                s = 0
        return res