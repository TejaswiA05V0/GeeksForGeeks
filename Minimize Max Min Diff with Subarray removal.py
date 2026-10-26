class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
            from itertools import accumulate
            if k == 0:
                return max(arr) - min(arr)
            n = len(arr)
            if k == n - 1:
                return 0
            prefix_min = list(accumulate(arr[:n - k], min, initial=10**9))
            prefix_max = list(accumulate(arr[:n - k], max, initial=1))
            diff = prefix_max[-1] - prefix_min[-1]
            suffix_min = suffix_max = arr[-1]
            for i in range(n - 1, k - 1, -1):
                if arr[i] < suffix_min:
                    suffix_min = arr[i]
                elif arr[i] > suffix_max:
                    suffix_max = arr[i]
                diff = min(diff, max(prefix_max[i - k], suffix_max) - min(prefix_min[i - k], suffix_min))
            return diff
        
