class Solution:
    def ways(self, x: int, y: int) -> int:
        # code here
        mat=[[0 for i in range(y+1)]for _ in range(x+1)]
        mat[0][0]=1
        MOD=1000000007
        for i in range(x+1):
            for j in range(y+1):
                up=left=0
                if i-1>=0:
                    up=mat[i-1][j]
                if j-1>=0:
                    left=mat[i][j-1]
                mat[i][j]+=up+left
                mat[i][j]%=MOD
        return mat[x][y]
