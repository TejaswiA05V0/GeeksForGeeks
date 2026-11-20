class Solution:
    def minFlips(self, s):
            n = len(s)
            even_ones = sum(c == "1" for c in s[::2])
            odd_ones = sum(c == "1" for c in s[1::2])
            return min(
                # ones on even indices
                (n + 1) // 2 - even_ones + odd_ones,
                # ones on odd indices
                n // 2 - odd_ones + even_ones,
            )
