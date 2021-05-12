class NumMatrix:
    def __init__(self, M: List[List[int]]):
        ylen, xlen = len(M) + 1, len(M[0]) + 1
        self.dp = [[0] * xlen for _ in range(ylen)]
        for i in range(1, ylen):
            for j in range(1, xlen):
                self.dp[i][j] = M[i-1][j-1] + self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1]

    def sumRegion(self, R1: int, C1: int, R2: int, C2: int) -> int:
        return self.dp[R2+1][C2+1] - self.dp[R2+1][C1] - self.dp[R1][C2+1] + self.dp[R1][C1]

    
    
    
    