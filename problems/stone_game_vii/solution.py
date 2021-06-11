class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        N=len(stones)
        CS = [0]
        for x in stones:
            CS.append(CS[-1]+x)
        assert(len(CS)==N+1)
        l = 0 # length of subarray
        R = [0 for _ in range(N+1)] # R[a] means beast score for stones[a:a+l]
        while l<N: # will stop at l==N
            #print("l=%d:"%l, R)
            l += 1
            prevR = R
            R = [] # will construct anew
            for i in range(N+1-l):
                # will solve for stones[i:i+l] and save result to R[i]
                score1 = CS[i+l-1] - CS[i] - prevR[i] # take the rightmost
                score2 = CS[i+l] - CS[i+1] - prevR[i+1] # the leftmost
                R.append(max(score1,score2))
        assert(len(R)==1)
        return R[0]
