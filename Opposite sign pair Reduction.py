class Solution:
    def reducePairs(self, arr):
        stack = []
        
        for num in arr:
            while stack and stack[-1] * num < 0:  # opposite signs
                if abs(stack[-1]) > abs(num):
                    num = None
                    break
                elif abs(stack[-1]) < abs(num):
                    stack.pop()
                else:
                    stack.pop()
                    num = None
                    break
            
            if num is not None:
                stack.append(num)
        
        return stack
