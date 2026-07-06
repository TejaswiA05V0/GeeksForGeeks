class Solution:
    def solve(self, i, array_index, a, b, am, bm, dp):
        arr = a if array_index == 0 else b

        if i >= len(arr):
            return 0

        if dp[array_index][i] != -1:
            return dp[array_index][i]

        curr = arr[i]

        if curr in am and curr in bm:
            left = self.solve(am[curr] + 1, 0, a, b, am, bm, dp)
            right = self.solve(bm[curr] + 1, 1, a, b, am, bm, dp)
            dp[array_index][i] = max(left, right)
        else:
            dp[array_index][i] = self.solve(i + 1, array_index, a, b, am, bm, dp)

        dp[array_index][i] += curr
        return dp[array_index][i]

    def maxPathSum(self, a, b):
        n, m = len(a), len(b)

        am = {x: i for i, x in enumerate(a)}
        bm = {x: i for i, x in enumerate(b)}

        dp = [[-1] * max(n, m) for _ in range(2)]

        return max(
            self.solve(0, 0, a, b, am, bm, dp),
            self.solve(0, 1, a, b, am, bm, dp)
        )
