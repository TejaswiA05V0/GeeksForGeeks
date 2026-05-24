class Solution:
    def coin(self, arr):
        # code here
        return sorted(arr)[0]
S=Solution()
n=int(input())
print(S.coin(arr))
