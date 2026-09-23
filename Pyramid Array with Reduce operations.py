class Solution:
    def formPyramid(self, arr):
           # code here 
           n = len(arr)
           left = [1]*n

           for i in range(1, n):
               left[i] = min(left[i-1]+1, arr[i])

           right = [1]*n
           for i in range(n-2, -1, -1):
               right[i] = min(right[i+1]+1, arr[i])

           h = max(min(h1, h2) for h1, h2 in zip(left, right))
           return sum(arr) - (1+h)*h + h
