class Solution:
    def isBinaryPalindrome(self, n):
        # code here
        res = ''
        while n > 0:
            res = str(n & 1) + res
            n >>= 1 
        binary = res
        if binary == binary[::-1]:
            return True
        return False

