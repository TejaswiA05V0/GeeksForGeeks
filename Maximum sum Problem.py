from collections import deque
class Solution:
    def maxSum(self, n):
        # code here
        q = deque()
        q.append(n)
        res=0
        while q:
            val = q.popleft()
            c1 = val//2
            c2 = val//3
            c3 = val//4
            if val<(c1+c2+c3):
                q.append(c1)
                q.append(c2)
                q.append(c3)
            else:
                res+=val
            # print(q)
        return res
