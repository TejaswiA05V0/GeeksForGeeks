class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        # code here
        t = n * m
        p = t * (t - 1)
      
        if n - 2 > 0 and m - 1 > 0:
            p -= 4 * (n - 2) * (m - 1)
            
        if n - 1 > 0 and m - 2 > 0:
            p -= 4 * (n - 1) * (m - 2)
            
        return p
s=Solution()
n=int(input())
m=int(input())
print(s.numOfWays(n,m))
