class Solution:
    def findPattern(self, s):
        # code here
        xs = 0
        ys = 0
        
        for l in s:
            if l == "x":
                if ys != 0:
                    return False
                else:
                    xs += 1
            elif l == "y":
                ys += 1
                if ys > xs:
                    return False
                elif ys == xs:
                    xs = ys = 0
        # Check for trailing x's
        return True if xs == 0 else False
