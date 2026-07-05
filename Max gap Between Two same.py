class Solution:

    def maxCharGap(self, s: str) -> int:
        first_i = {}
        max_dist = -1
        for i, c in enumerate(s):
            if c in first_i:
                if (d := i - first_i[c] - 1) > max_dist:
                    max_dist = d
            else:
                first_i[c] = i
        return max_dist

