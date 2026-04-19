class Solution:
    def isPower(self,x,y):
        # Edge case
        if x == 1:
            return y == 1
        
        # Divide y by x repeatedly
        while y % x == 0:
            y = y // x
        
        return y == 1
obj=Solution()
x=int(input())
y=int(input())
print(obj.isPower(x,y))
