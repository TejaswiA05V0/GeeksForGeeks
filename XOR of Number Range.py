class Solution:
    def findXOR(self, l: int, r: int) -> int:
            # code here
            ans = 0
            if l&1 != 0:
                ans = l
                l += 1

            re = (r-l+1)%4
            for k in range(re):
                ans ^= (r-k)
            return ans
