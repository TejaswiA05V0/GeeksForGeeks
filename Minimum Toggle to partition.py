class Solution:
    def minToggle(self, arr):
        # code here
        zeros = len(arr)-sum(arr)
        
        min_toggles = zeros
        curr_toggles = zeros
        
        for num in arr:
            if num == 1:
                curr_toggles += 1
            else:
                curr_toggles -= 1
            
            min_toggles = min(min_toggles, curr_toggles)
            
        return min_toggles
