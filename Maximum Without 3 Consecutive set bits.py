class Solution:
    def maxValue(self, n: int) -> int:
            if n == 0:
                return 0
            mask = 1 << n.bit_length() - 1
            answer, ones = n, 0
            while mask > 0:
                if mask & n:
                    ones += 1
                    if ones == 3:
                        answer ^= mask
                        ones = 0
                else:
                    ones = 0
                mask >>= 1
            return answer
