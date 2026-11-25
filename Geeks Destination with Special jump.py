class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        # code here
        MOD = 10**9 + 7
        gap = a - b
        def get_sum_of_quotients(N, K):
            if N < 0:
                return 0
            q = N // K
            rem = N % K
            return K * (q * (q - 1) // 2) + q * (rem + 1)
        count = r - l + 1
        part1_total = (d + 1) * count - count * (l + r) // 2
        limit_idx = d - a - 1
        effective_r = min(r, limit_idx)
        part2_total = 0
        if l <= effective_r:
            max_X = d - l - a + gap - 1
            min_X = d - effective_r - a + gap - 1
            sum_k = (
                get_sum_of_quotients(max_X, gap)
                - get_sum_of_quotients(min_X - 1, gap)
            )
            part2_total = 2 * b * sum_k
        return (part1_total + part2_total) % MOD
