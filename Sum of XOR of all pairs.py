class Solution:
    def sumXOR(self, arr):
        n = len(arr)
        result = 0
        
        for i in range(31, -1, -1):
            count_set = 0
            count_unset = 0
            
            for num in arr:
                if (num >> i) & 1:
                    count_set += 1
                else:
                    count_unset += 1
            
            result += (1 << i) * count_set * count_unset
        
        return result

