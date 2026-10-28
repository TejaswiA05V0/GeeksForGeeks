class Solution:
    def nthCharacter(self, n):
        # code here
        i=1
        totalCount=0
        while totalCount<n:
            totalCount+=(((10**i))-10**(i-1))*i
            # print(totalCount)
            if totalCount>=n:
                break
            i+=1
        low=10**(i-1)
        high=10**(i)-1
        resInt=low
        baseCount=totalCount-((high-low+1)*i)
        base=low
        # print(low,high,baseCount,totalCount)
        while low<=high:
            mid=low+(high-low)//2
            
            totalCharCount=baseCount+((mid-base+1)*i)
            # print(totalCharCount,mid)
            
            if totalCharCount>=n:
                resInt=mid
                high=mid-1
            else:
                low=mid+1
        totalCharCount=baseCount+(resInt-base+1)*i
        extraChar=totalCharCount-n
        for _ in range(extraChar):
            resInt//=10
        return str(resInt%10)
