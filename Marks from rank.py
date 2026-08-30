class Solution:
    def getMarks(self, l, r, rank):
        """code here"""
        all_marks={}
        n=len(l)
        pos=1
        for i in range(n):
           for val in range(l[i],r[i]+1):
             all_marks[pos]=val
             pos+=1
        res=[]
        for r in rank:
            res.append(all_marks[r])
        return res
