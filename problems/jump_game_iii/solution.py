class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        aj = {}
        for i in range(len(arr)):
            aj[i] = []
        for i in range(len(arr)):
            if i - arr[i] >= 0:
                aj[i].append(i - arr[i])
            if i + arr[i] < len(arr):
                aj[i].append(i + arr[i])
            aj[i] = list(set(aj[i]))
        print(aj)
        q = [start]
        visited = [False]*len(arr)
        while len(q) != 0:
            tmp = q.pop()
            if visited[tmp]: continue
            visited[tmp] = True
            if len(aj[tmp]) != 0:
                for j in aj[tmp]:
                    if j == tmp: return True
                    if visited[j]: continue
                    q.append(j)
        return False
                       