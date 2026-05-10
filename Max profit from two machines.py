class Solution:
    def maxProfit(self, x, y, a, b):
        n = len(a)

        # Store (difference, index)
        tasks = []
        for i in range(n):
            tasks.append((abs(a[i] - b[i]), i))

        # Sort by descending difference
        tasks.sort(reverse=True)

        profit = 0

        for _, i in tasks:
            # Prefer machine with higher profit
            if (a[i] >= b[i] and x > 0) or y == 0:
                profit += a[i]
                x -= 1
            else:
                profit += b[i]
                y -= 1

        return profit
