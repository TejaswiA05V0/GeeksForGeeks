class Solution:
    def smallestSubstring(self, s):
        n = len(s)
        count = {'0': 0, '1': 0, '2': 0}

        left = 0
        ans = float('inf')

        for right in range(n):
            count[s[right]] += 1

            # Shrink window while all three exist
            while count['0'] > 0 and count['1'] > 0 and count['2'] > 0:
                ans = min(ans, right - left + 1)

                count[s[left]] -= 1
                left += 1

        return ans if ans != float('inf') else -1
