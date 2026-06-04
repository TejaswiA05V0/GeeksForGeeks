class Solution:
    def maxSubstring(self, s):
        if not s:
            return 0

        max_current = max_global = (1 if s[0] == '0' else -1)
    
        for c in s[1:]:
            current = 1 if c == '0' else -1
            max_current = max(current, max_current + current)
            if max_current > max_global:
                max_global = max_current
    
        return max_global
