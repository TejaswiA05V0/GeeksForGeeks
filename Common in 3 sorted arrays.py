class Solution:
    def commonElements(self, a, b, c):
        # code here
        #Easiest way
        result = set(a)&set(b)&set(c)
        return sorted(list(result))
