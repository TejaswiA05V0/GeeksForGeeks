class Solution:
    def wifiRange(self, s, x):
        prv0=float('inf')
        prv1=-prv0
        for ix,ve in enumerate(s):
            if ve=='1':
                if prv0+x<ix:
                    return False
                prv0=float('inf')
                prv1=ix
            elif prv1+x<ix:
                prv0=min(ix,prv0)
        return prv0==float('inf')
