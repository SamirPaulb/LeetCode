class Solution:
    def multiply(self, n1: str, n2: str) -> str:
        n = len(n1)
        m = len(n2)
        arr = [0 for i in range(n+m)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                multi = int(n1[i])*int(n2[j])
                s = arr[i+j+1] 
                s += multi
                arr[i+j+1] = s % 10
                arr[i+j] += s // 10
        ans =""
        print(arr)
        for i in range(n+m):
            ans += str(arr[i])
        ans = int(ans)
        ans = str(ans)
        return ans
    