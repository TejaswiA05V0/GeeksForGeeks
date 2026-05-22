class Solution:
    def cntOnes(self, grid):
        hth=len(grid)
        wth=len(grid[0])
        pr=[*range(hth*wth+1)]
        sz=[1]*(hth*wth+1)
        def find(a):
            ori=a
            while pr[a]!=a:
                a=pr[a]
            pr[ori]=a
            return a
        def union(a,b):
            a=find(a)
            b=find(b)
            if a==b:
                return False
            if sz[a]>sz[b]:
                a,b=b,a
            pr[a]=b
            sz[b]+=sz[a]
            return True
        cnt=0
        for y in range(hth):
            for x in range(wth):
                if grid[y][x]==1:
                    cnt+=1
                    if y+1>=hth:
                        union(y*wth+x,wth*hth)
                    elif grid[y+1][x]==1:
                        union(y*wth+x,(y+1)*wth+x)
                    if y-1<0:
                        union(y*wth+x,wth*hth)
                    elif grid[y-1][x]==1:
                        union(y*wth+x,(y-1)*wth+x)
                    if x+1>=wth:
                        union(y*wth+x,wth*hth)
                    elif grid[y][x+1]==1:
                        union(y*wth+x,y*wth+x)
                    if x-1<0:
                        union(y*wth+x,wth*hth)
                    elif grid[y][x-1]==1:
                        union(y*wth+x,y*wth+x-1)
        return cnt-sz[find(wth*hth)]+1

