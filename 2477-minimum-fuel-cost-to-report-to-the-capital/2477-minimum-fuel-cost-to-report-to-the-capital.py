class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = defaultdict(list)
        for a, b in roads: adj[a].append(b), adj[b].append(a)
        
        visited = set()
        self.res = 0
        
        def dfs(city):
            if city in visited: return 0
            visited.add(city)
            totalCityCount = 0
            for c in adj[city]:
                curCityCount = dfs(c)
                self.res += math.ceil(curCityCount / seats) 
                totalCityCount += curCityCount
            return totalCityCount + 1
        
        dfs(0)
        return self.res
                