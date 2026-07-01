class Solution:
    def maxSumSubarray(self, arr):
        noDel = arr[0]
        oneDel = float('-inf')
        ans = arr[0]

        for i in range(1, len(arr)):
            oneDel = max(noDel, oneDel + arr[i])
            noDel = max(arr[i], noDel + arr[i])
            ans = max(ans, noDel, oneDel)

        return ans
