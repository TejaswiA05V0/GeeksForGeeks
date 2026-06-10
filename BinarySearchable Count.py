class Solution:
    def Possibles(self, low, high, arr, l, r):
        if l > r or low > high:
            return 0
            
        mid = (l + r) // 2
        right = max(low, arr[mid]), high
        left = low, min(arr[mid], high)
        curr = 0
        if low <= arr[mid] <= high:
            curr += 1
        curr += self.Possibles(*right, arr, mid + 1, r)
        curr += self.Possibles(*left, arr, l, mid - 1)
        return curr
        
    def binarySearchable(self, arr):
        # code here 
        low = -sys.maxsize
        high = sys.maxsize
        mid = len(arr) // 2
        return self.Possibles(low, high, arr, 0, len(arr) - 1)
