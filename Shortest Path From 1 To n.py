class Solution:
    def minimumStep (self, n):
        ret=-1
        while n:
            ret+=1
            if n%3==0:
                n//=3
            else:
                n-=1
        return ret
