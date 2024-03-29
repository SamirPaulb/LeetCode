class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = {}
        
        def addtoadjlist(a,b,v):
            if a not in adjList: adjList[a] = {(b,v)}
            else: adjList[a].add((b,v))
            if b not in adjList and v != 0: adjList[b] = {(a,1/v)}
            elif v != 0: adjList[b].add((a,1/v))
                
        for (a,b), v in zip(equations, values):
            addtoadjlist(a,b,v)
        
        res = []
        for a,b in queries:
            if a not in adjList or b not in adjList: res.append(-1); continue
            if a == b: res.append(1); continue
            q = collections.deque()
            q.append((1,a))
            visited = set()
            got = False
            while q:
                v,c = q.popleft()
                if c in visited: continue
                if c == b: res.append(v); got = True; break
                visited.add(c)
                addtoadjlist(a,c,v)
                for nc, nv in adjList[c]:
                    q.append((v*nv, nc))
            if not got: res.append(-1)
        # print(adjList)
        return res
                