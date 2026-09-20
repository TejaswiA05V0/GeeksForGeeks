class Solution:
    def largestSubsquare(self, mat):
#code here
        n = len(mat)
        # dp[r][c] = (r, c)
        dp = [[(0, 0)]*(n+1) for _ in range(n+1)]
        for r in range(n-1, -1, -1):
            for c in range(n-1, -1, -1):
                if mat[r][c] == 'X':
                    dr = dp[r][c+1][0]+1
                    dc = dp[r+1][c][1]+1
                    dp[r][c] = (dr, dc)
                    
        ans = 0
        for r0 in range(n):
            for c0 in range(n):
                m = min(dp[r0][c0])
                for k in range(1, m+1):
                    r = r0+k-1
                    c = c0+k-1
                    k1 = dp[r][c0][0]
                    k2 = dp[r0][c][1]
                    if k1 >= k and k2 >= k:
                        ans = max(ans, k)
        return ans
