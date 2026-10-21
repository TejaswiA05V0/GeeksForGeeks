class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        gmn=min(arr)
        lmn=0
        for ve in arr:
            lmn+=ve
            lmn=min(lmn,ve)
            gmn=min(gmn,lmn)
        return gmn
