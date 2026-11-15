class Solution:
    def subsequenceSum(self, s):
            """code here"""
            M = 10**9+7
            n = len(s)
            if n == 1:
                return int(s)
            ways = pow(2, n-1, M)
            return sum(int(d)*ways%M for d in s)%M
