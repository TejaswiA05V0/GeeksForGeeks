class Solution:
    def checkElements(self, start, end, arr):
        # code here
        b=(end-start)+1
        c=0
        arr=set(arr)
        for i in range(start,end+1):
            if i in arr:
                c+=1
        return b==c
