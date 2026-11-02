class Solution:
    def largestSumCycle(self, edge):
        from collections import defaultdict
        ino=defaultdict(int)
        adj=defaultdict(set)
        for cur,nxt in enumerate(edge):
            if nxt==-1:
                continue
            ino[nxt]+=1
            adj[cur].add(nxt)
        lth=len(edge)
        q=[v for v in range(lth) if ino[v]==0]
        while q:
            cur=q.pop()
            for nxt in adj[cur]:
                ino[nxt]-=1
                if ino[nxt]==0:
                    q.append(nxt)
        seen=set()
        def dfs(cur):
            nonlocal adj,seen
            if cur in seen:
                return 0
            seen.add(cur)
            return dfs(list(adj[cur])[0])+cur
        mx=-1
        for cur in [v for v in range(lth) if ino[v]>0]:
            mx=max(mx,dfs(cur))
        return mx

