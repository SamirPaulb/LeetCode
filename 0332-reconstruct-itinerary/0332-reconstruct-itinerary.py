class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for scr, dst in tickets:
            if scr not in adj:
                adj[scr] = [dst]
            else:
                adj[scr].append(dst)
        
        for scr in adj:
            adj[scr].sort(reverse = True)
        
        stack = ['JFK']
        res = []
        while stack:
            elm = stack[-1]
            if elm in adj and len(adj[elm]) > 0:
                stack.append(adj[elm].pop())
            else:
                res.append(stack.pop())
        
        return res[::-1]