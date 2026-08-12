class Solution:
    def findWays(self, grid):
        # code here
        n=len(grid)
        maxAdventure=[[0 for i in range(n)]for _ in range(n)]
        totalPaths=[[0 for i in range(n)]for _ in range(n)]
        vis=[[0 for i in range(n)]for j in range(n)]
        maxAdventure[0][0]=grid[0][0]
        totalPaths[0][0]=1
        vis[0][0]=1
        
        for i in range(1,n):
            if grid[0][i-1]==1 or grid[0][i-1]==3:
                maxAdventure[0][i]+=maxAdventure[0][i-1]+grid[0][i]
                totalPaths[0][i]=1
                vis[0][i]=1
            else:
                break
            
        for i in range(1,n):
            if grid[i-1][0]==2 or grid[i-1][0]==3:
                maxAdventure[i][0]+=maxAdventure[i-1][0]+grid[i][0]
                totalPaths[i][0]=1
                vis[i][0]=1
            else:
                break
            
        for i in range(1,n):
            for j in range(1,n):
                if vis[i][j-1] and (grid[i][j-1]==1 or grid[i][j-1]==3):
                    maxAdventure[i][j]=max(maxAdventure[i][j],maxAdventure[i][j-1]+grid[i][j])
                    totalPaths[i][j]+=totalPaths[i][j-1]
                    vis[i][j]=1

                if vis[i-1][j] and (grid[i-1][j]==2 or grid[i-1][j]==3):
                    maxAdventure[i][j]=max(maxAdventure[i][j],maxAdventure[i-1][j]+grid[i][j])
                    totalPaths[i][j]+=totalPaths[i-1][j]
                    vis[i][j]=1
                totalPaths[i][j]%=1000000007
        return [totalPaths[-1][-1],maxAdventure[-1][-1]]
