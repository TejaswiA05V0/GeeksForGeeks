class Solution:
    def smallestSubWithSum(self, arr, x):
        mn=float('inf')
        sm=l=0
        for r in range(len(arr)):
            sm+=arr[r]
            while sm>x:
                mn=min(mn,r-l+1)
                sm-=arr[l]
                l+=1
        return mn if mn<float('inf') else 0
