class Solution:
    def maximumSubarray(self, arr: list[int]) -> int:
           n = len(arr)
           prefix_max = [0] * n
           for i in range(n - 1):
               prefix_max[i + 1] = max(prefix_max[i] + arr[i], 0)
           suffix_max = [0] * n
           for i in range(n - 1, 0, -1):
               suffix_max[i - 1] = max(suffix_max[i] + arr[i], 0)
           return max(prefix_max[i] + arr[i]**2 + suffix_max[i] for i in range(n))
