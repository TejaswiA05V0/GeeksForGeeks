class Solution:
    def getLastDigit(self, a, b):
        # code here
        if b=='0':
            return 1
        return pow(int(a[-1]),int(b),10)
