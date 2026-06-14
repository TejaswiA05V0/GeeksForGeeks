class Solution:
    dxn=[(0,1),(1,0),(0,-1),(-1,0)]
    def exitPoint(self, mat):
        n,m=len(mat),len(mat[0])
        ans=[0,0]
        p,i,j=0,0,0
        while 0<=i<n and 0<=j<m:
            if mat[i][j]==0:
                ans=[i,j]
                dx,dy=Solution.dxn[p]
                i+=dx
                j+=dy
            else:
                mat[i][j]=0
                p=(p+1)%4
        return ans
