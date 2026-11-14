class Solution:
    def maxEqualSum(self, s1: list[int], s2: list[int], s3: list[int]) -> int:
        # code here
        a1=0;
        a2=0;
        a3=0;
        
        p=len(s1)
        q=len(s2)
        r=len(s3)
        
        for x in s1 :
            a1+=x
        for x in s2:
            a2+=x
        for x in s3:
            a3+=x
        
        i=0
        j=0
        k=0
        
        while i<p and j<q and k<r :
            if a1==a2 and a2==a3 and a3==a1:
                return a1
            
            if a1<=a2 and a2<=a3:
                a3-=s3[k]
                k+=1
            elif a1<=a3 and a3<=a2:
                a2-=s2[j]
                j+=1
            elif a2<=a1 and a1<=a3:
                a3-=s3[k]
                k+=1
            elif a2<=a3 and a3<=a1:
                a1-=s1[i]
                i+=1
            elif a3<=a1 and a1<=a2:
                a2-=s2[j]
                j+=1
            elif a3<=a2 and a2<=a1:
                a1-=s1[i]
                i+=1
            
        
        return 0
