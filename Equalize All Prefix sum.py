class Solution:
    def optimalArray(self, arr):
        ans = []
        for i,ele in enumerate(arr):
            med = i//2
            take = 0 if i==0 else abs(ans[i-1]+arr[i]-arr[med])
            ans.append(take)
        return ans
