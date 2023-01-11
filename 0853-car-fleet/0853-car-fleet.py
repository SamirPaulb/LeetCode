class Solution:
    def carFleet(self, target, position, speed):
        ps = [(p,s) for p,s in zip(position, speed)]
        ps.sort()
        time = []
        for p, s in ps:
            t = (target - p) / s
            time.append(t)
        # print(time)
        rmax = res = 0
        for t in time[::-1]:
            if t > rmax:
                rmax = t
                res += 1
        
        return res