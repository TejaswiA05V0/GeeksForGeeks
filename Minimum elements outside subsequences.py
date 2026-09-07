class Solution:
    def minCount(self, arr):
            """ code here """
            from functools import cache

            n = len(arr)
            @cache
            def count(pos, inc_idx=-1, dec_idx=-1):
                nonlocal n
                if pos == n:
                    return 0
                cnt = count(pos+1, inc_idx, dec_idx)
                if inc_idx == -1 or arr[pos] > arr[inc_idx]:
                    cnt = max(cnt, count(pos+1, pos, dec_idx)+1)
                if dec_idx == -1 or arr[pos] < arr[dec_idx]:
                    cnt = max(cnt, count(pos+1, inc_idx, pos)+1)

                return cnt
            return n-count(0)
