class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n=len(edges)
        bl=[0]*n
        mp=defaultdict(int)
        mx=-1
        for i in range(n):
            if(bl[i]==0):
                x=i
                l=0
                st=set()
                while x>-1 and bl[x]==0:
                    bl[x]=1
                    mp[x]=l
                    l+=1
                    st.add(x)
                    x=edges[x]
                if(x!=-1 and x in st): mx=max(mx,l-mp[x])
        return mx
