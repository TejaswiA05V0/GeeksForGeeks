class Solution:
    def minMoves(self, arr):
        n = len(arr)
        dp = {}
        max_len = 0
        
        for num in arr:
            # Length of sequence ending at 'num' is 1 + sequence length of 'num - 1'
            dp[num] = dp.get(num - 1, 0) + 1
            max_len = max(max_len, dp[num])
            
        return n - max_len
