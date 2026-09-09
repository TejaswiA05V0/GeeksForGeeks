class Solution:
    def findMax(self, n):
        ans = n
        maxSum = sum(map(int, str(n)))
        b = 1
        x = n

        while x > 0:
            candidate = (x - 1) * b + (b - 1)
            if candidate > 0:
                curr_sum = sum(map(int, str(candidate)))
                if curr_sum > maxSum or (curr_sum == maxSum and candidate > ans):
                    maxSum = curr_sum
                    ans = candidate
            x //= 10
            b *= 10

        return ans
