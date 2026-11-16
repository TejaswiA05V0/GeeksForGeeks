class Solution:
    def findKthSmall(self, arr, k):
        # code here
        arr.append(0)
        arr.sort()
        n=len(arr)
        for i in range(len(arr)-1):
            diff=arr[i+1]-arr[i]
            if k<diff:
                return arr[i]+k
            else:
                k-=(diff-1)
            
        
        return arr[n-1]+k
