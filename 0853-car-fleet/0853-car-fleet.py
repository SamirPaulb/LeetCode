class Solution:
    def carFleet(self, target, position, speed):
        ps = [(p,s) for p,s in zip(position, speed)]
        ps.sort()
        time = [(target-p)/s for p,s in ps]
        # print(time)
        rmax = res = 0
        for t in time[::-1]:
            if t > rmax:
                rmax = t
                res += 1
        
        return res